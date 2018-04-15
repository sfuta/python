#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" プロセスの並列化を実行
"""

import sys
import time
import subprocess
import multiprocessing as multi

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: [command [argv]]'
        exit(1)

    def call_process():
        """ コマンドに設定したプロセスを実行
        """
        subprocess.call(sys.argv[1:])

    while True:
        # 最大10回子プロセス起動
        while len(multi.active_children()) < 3:
            p = multi.Process(name='worker', target=call_process)
            p.start()
            # 次のプロセス作成前に0.1秒待ち
            time.sleep(0.1)

        # 1秒毎にプロセス数確認
        time.sleep(1)
