# coding=utf-8

__author__ = 'sinlov'

import io, sys, time, re, os, logging
import winreg

reload(sys)
sys.setdefaultencoding('utf8')

if not os.path.exists('log/'):
    os.makedirs('log/')

logging.basicConfig(level=logging.NOTSET,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log/' + str(time.strftime("%Y-%m-%d_%H_%M_%S")) + '.log',
                    filemode='w'
                    )

# IE 代理表项路径
xpath = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"

# 设定代理,enable:是否开启,proxyIp:代理服务器ip及端口,IgnoreIp:忽略代理的ip或网址
def set_proxy(enable, proxy_ip, ignore_ip):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, xpath, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, enable)
        winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxy_ip)
        winreg.SetValueEx(key, "ProxyOverride", 0, winreg.REG_SZ, ignore_ip)
    except Exception as e:
        logging.exception(str(e.message), e.args)
        print("ERROR: " + str(e.args))
    finally:
        None


# 开启，定义代理服务器ip及端口，忽略ip内容(分号分割)
def enable_proxy():
    proxy_ip = "172.21.18.21:8080"
    ignore_ip = "172.*;192.*;"
    print(" Setting proxy ")
    set_proxy(1, proxy_ip, ignore_ip)
    logging.info('Setting proxy ip: ' % proxy_ip)
    logging.info('Setting proxy ignore: ' % ignore_ip)
    print(" Setting success")


# 关闭清空代理
def disable_proxy():
    print(" Empty proxy")
    set_proxy(0, "", "")
    logging.info('disable proxy success')
    print(" Empty success")


def main():
    place = input("where are you?(home or lp)\n")
    try:
        if place == "home":
            disable_proxy()
        elif place == "lp":
            enable_proxy()
        else:
            print("please input 'home' or 'lp'(local proxy)!")
            main()
    except Exception as e:
        logging.exception('main exception' % e.args % e.message)
        print("ERROR: " + str(e.args))
    finally:
        pass


if __name__ == '__main__':
    main()
