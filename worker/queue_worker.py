# -*- coding: utf-8 -*-

import subprocess

"""
QueueWorkerの抽象クラス
"""
class QueueWorker(object):

    def __init__(self):
        """ コンストラクタ
        """
        self.worker_cmd  = None  # 実行コマンド
        self.retry_count = None  # リトライ回数

    def ready(self):
        """ 開始処理を記載(DB更新/ロギング等)
        """

    def pop_queue():
        """ キューからデータを取り出し、渡す
        """
        return None

    def end(self):
        """ 完了後処理を記載(DB更新/ロギング等)
        """

    def run(self, message):
        """ メイン取得処理を実行
        :param message string
        """
        # 開始処理
        self.ready()
        # タスク実行
        for i in range(self.retry_count):
            if self.call_worker_cmd(message):
                # 成功時は処理を抜ける
                break;
        # 終了処理
        self.end()

    def call_worker_cmd(self, message):
        """ 実処理の呼び出しを実行
        :param message string workerのパラメータ
        :return boolean 成功可否
        """
        # メッセージサイズが256KB超過している場合は例外を投げる
        if len(message) > 256 * 1024:
            raise ValueError("queue message is over limit. size:" + len(message))
        # worker_cmdにメッセージ(最大256KB)を渡して実行
        p = subprocess.Popen(self.worker_cmd, stdin=subprocess.PIPE)
        p.communicate(input=message)
        p.wait()
        return p.returncode == 0
