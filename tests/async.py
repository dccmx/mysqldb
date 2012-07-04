#!/usr/bin/env python
# coding: utf-8
import MySQLdb
import tornado.ioloop as ioloop


def main():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="test")

    def query_done(res):
        print 'result: ', res

    for i in range(5):
        print 'query'
        conn.async_query('SELECT sleep(1);', query_done)

    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
