#!/usr/bin/env python
# coding: utf-8
import MySQLdb
import tornado.ioloop as ioloop


def main():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="nodb")

    def query_done(res):
        print 'result: ', res
        conn.async_query('SELECT sleep(1);', query_done)

    for i in range(1):
        conn.async_query('SELECT sleep(1);', query_done)

    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
