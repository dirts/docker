#!/usr/bin/env python
#encoding=utf-8

def p1():
    print 'print p1'

class Cat:

    name        = ''
    __wieght    = 0

    def __init__(self, name, weight):
        self.name = name
        self.__weight = weight

    def miao(self, msg):
        print msg

    def getWeight(self):
        print self.__weight

    def __del__(self):
        print 'die'


class HeiCat(Cat):

    def run(self) :
        print 'runing'
