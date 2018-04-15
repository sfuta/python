#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import multiprocessing


class NeetsDaemon(object):

    def __init__(self, processes):
        self.processes = processes

    def start(self):
        for i in range(self.processes):
            # 新しいプロセスを作る
            p = multiprocessing.Process(target=self._main)
            # デーモンフラグを有効にすると親プロセスが死んだとき一緒に死ぬようになる
            p.daemon = True
            # プロセスを開始する
            p.start()
            p.join()

    def _main(self):
        print "start _main"
        for i in range(10):
            time.sleep(1)
            print "count:%s" % i

        print "end_main"

if __name__ == '__main__':
    # 子プロセスは 3 つ
    neetsd = NeetsDaemon(3)
    # デーモンを開始する
    neetsd.start()
