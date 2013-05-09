#!/usr/bin/env python
'''
Threading module code shamelessly stolen from Wesley Chun's massive book "Core Python Programming" 

'''
import threading

from time import ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print 'starting', self.name, 'at:', \
        ctime()
        self.res = apply(self.func, self.args)
        print self.name, 'finished at:', \
        ctime()
