# coding=utf-8

__author__ = 'sinlov'

import socket
import hashlib
import threading
import time
import struct
from base64 import b64encode, b64decode
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn

connection_list = {}
g_code_length = 0
g_header_length = 0


class RequestHandler(BaseHTTPRequestHandler):
    def handle_one_request(self):
        """Handle a single HTTP request.

        You normally don't need to override this method; see the class
        __doc__ string for information on how to handle specific HTTP
        commands such as GET and POST.

        """
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(414)
                return
            if not self.raw_requestline:
                self.close_connection = 1
                return
            if not self.parse_request():
                # An error code has been sent, just exit
                return
            mname = 'do_' + self.command
            if not hasattr(self, mname):
                self.send_error(501, "Unsupported method (%r)" % self.command)
                return
            method = getattr(self, mname)
            print "before call do_Get"
            method()
            # 增加 debug info 及 wfile 判断是否已经 close
            print "after call do_Get"
            if not self.wfile.closed:
                self.wfile.flush()  # actually send the response if not already done.
            print "after wfile.flush()"
        except socket.timeout, e:
            # a read or a write timed out.  Discard this connection
            self.log_error("Request timed out: %r", e)
            self.close_connection = 1
            return

    def do_GET(self):
        """
        处理get请求
        """
        query = self.path
        print "query: %s thread=%s" % (query, str(threading.current_thread()))

        ret_str = "<html>" + self.path + "<br>" + str(self.server) + "</html>"

        time.sleep(5)

        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(ret_str)
        except socket.error, e:
            print "socket.error : Connection broke. Aborting" + str(e)
            self.wfile._sock.close()
            self.wfile._sock = None
            return False

        print "success prod query :%s" % (query)
        return True


# 多线程处理
class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass


def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


def get_data_length(msg):
    global g_code_length
    global g_header_length

    print (len(msg))
    g_code_length = ord(msg[1]) & 127
    received_length = 0
    if g_code_length == 126:
        # g_code_length = msg[2:4]
        # g_code_length = (ord(msg[2])<<8) + (ord(msg[3]))
        g_code_length = struct.unpack('>H', str(msg[2:4]))[0]
        g_header_length = 8
    elif g_code_length == 127:
        # g_code_length = msg[2:10]
        g_code_length = struct.unpack('>Q', str(msg[2:10]))[0]
        g_header_length = 14
    else:
        g_header_length = 6
    g_code_length = int(g_code_length)
    return g_code_length


def parse_data(msg):
    global g_code_length
    g_code_length = ord(msg[1]) & 127
    received_length = 0
    if g_code_length == 126:
        g_code_length = struct.unpack('>H', str(msg[2:4]))[0]
        masks = msg[4:8]
        data = msg[8:]
    elif g_code_length == 127:
        g_code_length = struct.unpack('>Q', str(msg[2:10]))[0]
        masks = msg[10:14]
        data = msg[14:]
    else:
        masks = msg[2:6]
        data = msg[6:]
    i = 0
    raw_str = ''
    for d in data:
        raw_str += chr(ord(d) ^ ord(masks[i % 4]))
        i += 1
    print (u"msg length: %d" % int(g_code_length))
    return raw_str


def sendMessage(message):
    global connection_list

    message_utf_8 = message.encode('utf-8')
    for connection in connection_list.values():
        back_str = ['\x81']
        data_length = len(message_utf_8)

        if data_length <= 125:
            back_str.append(chr(data_length))
        elif data_length <= 65535:
            back_str.append(struct.pack('b', 126))
            back_str.append(struct.pack('>h', data_length))
            # back_str.append(chr(data_length >> 8))
            # back_str.append(chr(data_length & 0xFF))
            # a = struct.pack('>h', data_length)
            # b = chr(data_length >> 8)
            # c = chr(data_length & 0xFF)
        elif data_length <= (2 ^ 64 - 1):
            # back_str.append(chr(127))
            back_str.append(struct.pack('b', 127))
            back_str.append(struct.pack('>q', data_length))
            # back_str.append(chr(data_length >> 8))
            # back_str.append(chr(data_length & 0xFF))
        else:
            print (u'Your message is too long, max length is 65535')
        msg = ''
        for c in back_str:
            msg += c
        back_str = str(msg) + message_utf_8  # .encode('utf-8')
        # connection.send(str.encode(str(u"\x00%s\xFF\n\n" % message))) #这个是旧版
        # print (u'send message:' +  message)
        if back_str is not None and len(back_str) > 0:
            print ('connection.send ' + back_str)
            connection.send(back_str)


def delete_connection(item):
    global connection_list
    del connection_list['connection' + item]


class WebSocket(threading.Thread):  # 继承Thread

    GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

    def __init__(self, conn, index, name, remote, path="/"):
        threading.Thread.__init__(self)  # 初始化父类Thread
        self.conn = conn
        self.index = index
        self.name = name
        self.remote = remote
        self.path = path
        self.buffer = ""
        self.buffer_utf8 = ""
        self.length_buffer = 0

    def run(self):  # 重载Thread的run
        print('Socket%s Start!' % self.index)
        headers = {}
        self.hands_taken = False
        global g_code_length
        global g_header_length
        while True:
            if self.hands_taken == False:
                print ('Socket%s Start Handshaken with %s!' % (self.index, self.remote))
                self.buffer += bytes.decode(self.conn.recv(1024))

                if self.buffer.find('\r\n\r\n') != -1:
                    header, data = self.buffer.split('\r\n\r\n', 1)
                    for line in header.split("\r\n")[1:]:
                        key, value = line.split(": ", 1)
                        headers[key] = value

                    headers["Location"] = ("ws://%s%s" % (headers["Host"], self.path))
                    key = headers['Sec-WebSocket-Key']
                    token = b64encode(hashlib.sha1(str.encode(str(key + self.GUID))).digest())

                    handshake = "HTTP/1.1 101 Switching Protocols\r\n" \
                                "Upgrade: websocket\r\n" \
                                "Connection: Upgrade\r\n" \
                                "Sec-WebSocket-Accept: " + bytes.decode(token) + "\r\n" \
                                                                                 "WebSocket-Origin: " + str(
                        headers["Origin"]) + "\r\n" \
                                             "WebSocket-Location: " + str(headers["Location"]) + "\r\n\r\n"

                    self.conn.send(str.encode(str(handshake)))
                    self.hands_taken = True
                    print ('Socket %s Handshaken with %s success!' % (self.index, self.remote))
                    sendMessage(u'Welcome, ' + self.name + ' !' + '\n\tYou can disconnect with "quit"')
                    self.buffer_utf8 = ""
                    g_code_length = 0
            else:
                mm = self.conn.recv(128)
                if len(mm) <= 0:
                    continue
                if g_code_length == 0:
                    get_data_length(mm)
                # 接受的长度
                self.length_buffer += len(mm)
                self.buffer = self.buffer + mm
                if self.length_buffer - g_header_length < g_code_length:
                    continue
                else:
                    self.buffer_utf8 = parse_data(self.buffer)  # utf8
                    msg_unicode = str(self.buffer_utf8).decode('utf-8', 'ignore')  # unicode
                    if msg_unicode == 'quit':
                        print (u'Socket%s Logout!' % self.index)
                        now_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
                        sendMessage(
                            u'%s %s Logout callback: %s' % (now_time, self.remote, self.name + ' Logout success'))
                        delete_connection(str(self.index))
                        self.conn.close()
                        break  # 退出线程
                    else:
                        # print (u'Socket%s Got msg:%s from %s!' % (self.index, msg_unicode, self.remote))
                        now_time = time.strftime(u'%H:%M:%S', time.localtime(time.time()))
                        sendMessage(u'%s %s msg callback: %s' % (now_time, self.remote, msg_unicode))
                        # 重置buffer和buffer_length
                    self.buffer_utf8 = ""
                    self.buffer = ""
                    g_code_length = 0
                    self.length_buffer = 0
            self.buffer = ""


class WebSocketServer(object):
    def __init__(self):
        self.damon_name = "127.0.0.1"
        self.port_number = 30011
        self.socket = None

    def begin(self):
        print('WebSocketServer Start! info => ' + self.damon_name + ':' + str(self.port_number))
        print('\tYou can connect with => ws://' + self.damon_name + ':' + str(self.port_number))
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.damon_name, self.port_number))
        self.socket.listen(50)
        global connection_list
        i = 0
        while True:
            connection, address = self.socket.accept()
            username = address[0]
            new_socket = WebSocket(connection, i, username, address)
            new_socket.start()  # 开始线程,执行run函数
            connection_list['connection' + str(i)] = connection
            i += 1


if __name__ == "__main__":
    server = WebSocketServer()
    server.begin()
