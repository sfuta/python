#!/usr/bin/env python -B
# -*- coding: utf-8 -*-

""" プロセスの並列化を実行
"""

import sys
import time
import subprocess
import multiprocessing as multi
import logging
import signal

def main(argv):
    if len(argv) < 2:
        print 'Usage: [command [argv]]'
        exit(1)

    mylogger = logging.getLogger(__name__)
    # ログレベルの設定
    mylogger.setLevel(10)
    fh = logging.FileHandler('test.log')
    fh.setFormatter(logging.Formatter("[%(levelname)s][%(pathname)s(%(lineno)s)]:%(message)s"))
    mylogger.addHandler(fh)

    def handler(signum, frame):
        for p in multi.active_children():
            mylogger.info("Terminate={}".format(p.pid))
            p.terminate()
        exit(0)

    # Set the signal handler and a 5-second alarm
    signal.signal(signal.SIGTERM, handler)

    def call_process():
        """ コマンドに設定したプロセスを実行
        """
        try:
            p = subprocess.Popen(argv[1:])
            mylogger.info("Subprocess Start={}".format(p.pid))
            p.wait()
        except:
            mylogger.info("Child Terminate={}".format(p.pid))
            p.terminate()

        # def handler(signum, frame):
        #     mylogger.info("Terminate={}".format(p.pid))
        #     p.terminate()
        #
        # signal.signal(signal.SIGTERM, handler)

    try:
        while True:
            # 最大10回子プロセス起動
            while len(multi.active_children()) < 3:
                p = multi.Process(name='worker', target=call_process)
                # 親プロセスが死んだら,子プロセスも死ぬようにする
                # p.daemon = True
                p.start()
                mylogger.info("Make Process {}".format(p.pid))
                # 次のプロセス作成前に0.1秒待ち
                time.sleep(0.1)

            # 1秒毎にプロセス数確認
            time.sleep(1)
    except:
        for p in multi.active_children():
            mylogger.info("Parent Terminate={}".format(p.pid))
            p.terminate()

if __name__ == '__main__':
    main(sys.argv)
