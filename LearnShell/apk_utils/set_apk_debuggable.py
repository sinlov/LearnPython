# coding=utf-8

__author__ = 'sinlov'

import os
import xml.etree.ElementTree as ET
import logging
import logging.handlers
import ConfigParser

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

ANDROID_NAMESPACE = 'http://schemas.android.com/apk/res/android'
ET.register_namespace('android', ANDROID_NAMESPACE)
debuggableKey = '{' + ANDROID_NAMESPACE + '}debuggable'
LOG_FILE = 'set_apk_debuggable.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('set_apk_debuggable')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


class PrettyConfigParser(ConfigParser.ConfigParser):
    def optionxform(self, option):
        return option


reload(sys)
sys.setdefaultencoding('utf8')


is_open_debug = False

def change_apk_debuggable(mamifest):
    global is_open_debug
    ET.register_namespace('android', ANDROID_NAMESPACE)
    rootTree = ET.parse(mamifest)
    root = rootTree.getroot()
    applicationNode = root.find("application")
    if applicationNode is None:
        logger.error('do not found application at => ' + mamifest)
        return
    debugKey = applicationNode.get(debuggableKey)
    logger.info('this app debugKey is ' + debugKey)
    if is_open_debug:
        applicationNode.set(debuggableKey, 'true')
    else:
        applicationNode.set(debuggableKey, 'false')
    rootTree.write(mamifest, 'UTF-8')
    logger.info('change apk_debuggable success at => ' + is_open_debug + " " + mamifest)


def change_log_print(sdkParams):
    global is_open_debug
    if not os.path.exists(sdkParams):
        logger.error('do not found sdkParams.properties at => ' + sdkParams)
    else:
        dev_cf = PrettyConfigParser()
        dev_cf.read(sdkParams)
        print('' + dev_cf.get('matrix', 'debugMode'))
        if is_open_debug:
            dev_cf.set('matrix', 'debugMode', 0)
        else:
            dev_cf.set('matrix', 'debugMode', 1)
        file_io = open(sdkParams, 'w')
        dev_cf.write(file_io)
        file_io.close()
        logger.info('change Log print success at => ' + is_open_debug + " " + sdkParams)


def path_skip_move(path, is_open=False):
    global is_open_debug
    is_open_debug = is_open
    change_apk_debuggable(path + "/AndroidManifest.xml")
    change_log_print(path + '/assets/sdkParams.properties')

if __name__ == '__main__':
    try:
        if cmp(sys.argv[2], "1") == 0:
            path_skip_move(sys.argv[1], True)
        else:
            path_skip_move(sys.argv[1], False)
        print "---------------change_apk_debuggable success-----------------------"
        pass
    except Exception, e:
        print "---------------your path is error-----------------------"
        raise e
