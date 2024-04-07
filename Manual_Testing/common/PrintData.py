# -*- coding: utf-8 -*-
import sys


class Logger(object):
    def __init__(self, filename='E:\pythonProject\insure\Manual_Testing\ResponseLog.js', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a', encoding='utf-8')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

# sys.stdout = Logger()
# sys.stderr = Logger()

# print("Hello World")
