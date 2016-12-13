#!/usr/bin/env python
#encoding=utf-8
def say():
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [u"This is hello wsgi app".encode('utf8')]

class Person:
    def __init__ (self):
        self.name = 'Persion'

    def hello(self) :
        print 'hellow'
