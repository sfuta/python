# -*- coding: utf-8 -*-

from queue_worker import QueueWorker
import time
import os

"""
SampleWorker管理クラス
"""
class SampleQueueWorker(QueueWorker):

    def __init__(self):
        self.retry_count = 2
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.worker_cmd  = ("python", current_dir + "/sample_cmd.py")

    def ready(self):
        """ 開始処理(DB更新/ロギング等)
        """
        print "START Sample Queue"

    def end(self):
        """ 完了後処理を記載(DB更新/ロギング等)
        """
        print "End Sample Queue"

    def pop_queue(self):
        """ キューからデータを取り出し、渡す
        """
        time.sleep(5)
        return "AAAAAAAAAAAAAAAAA"
