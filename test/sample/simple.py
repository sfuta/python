#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import multiprocessing as multi

def child_process():
    for i in range(10):
        sys.stdout.write("%s " % i)
        time.sleep(1)
    print ""

if __name__ == '__main__':

    while True:
        # 最大10回子プロセス起動
        while len(multi.active_children()) < 10:
            p = multi.Process(name='worker', target=child_process)
            p.start()
            # 次のプロセス作成前に0.1秒待ち
            time.sleep(0.1)

        # 1秒毎にプロセス数確認
        time.sleep(1)

