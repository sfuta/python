#!/usr/bin/env python -B
# -*- coding: utf-8 -*-

import re
import sys

""" queue_worker系実行スクリプト
"""
def main(argv):

    # クラスのメタ情報取得
    task_name   = argv[1]
    class_name  = task_name + "QueueWorker"
    dir_name    = re.sub("([A-Z])", lambda x:x.group(1).lower(), task_name)
    file_name   = re.sub("([A-Z])", lambda x:"_" + x.group(1).lower(), task_name)[1:]
    module_name = dir_name + "." + file_name + "_queue_worker"

    # メタ情報からインスタンス作成
    module = __import__(module_name, fromlist=[class_name])
    worker = getattr(module, class_name)
    w = worker()

    # クラス定義に従い、workerを実行
    while True:
        message = w.pop_queue()
        if message:
            w.run(message)

if __name__ == '__main__':
    main(sys.argv)
