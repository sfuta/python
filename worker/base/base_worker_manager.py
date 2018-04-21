# -*- coding: utf-8 -*-

import subprocess

"""
worker管理基底クラス
"""
class BaseWorkerManager(object):

    def __init__(self):
        """ 利用クラスのインスタンス化等
        """
        # 実行コマンド
        self.worker_cmd = ("python", "default_worker")
        # 試行回数
        self.retry_count = 1

    def ready(self):
        """ 開始処理を記載(DB更新/ロギング等)
        """

    def end(self):
        """ 完了後処理を記載(DB更新/ロギング等)
        """

    def pop_queue():
        """ キューからデータを取り出し、渡す
        """
        return None


    def run(self):
        """ メイン取得処理を実行
        :param retry_count int 試行回数
        """
        # キューからパラメータ取得
        message = self.pop_queue()

        # 開始前処理を実行
        self.ready()

        # タスク実行
        for i in range(self.retry_count):
            if self.call_worker(message):
                # 成功時は処理を抜ける
                break;
            # 次の実行まで1秒,waitする
            sleep(1)

        # 終了処理を実行
        self.end()

    def call_worker(self, message):
        """ worker処理の呼び出しを実行
        :param message string workerのパラメータ
        :return boolean 成功可否
        """
        # メッセージサイズが256KB超過している場合は例外を投げる
        if len(message) > 256 * 1024:
            raise ValueError("queue message is over limit. size:" + len(message))

        # workerにメッセージ(最大256KB)を渡して実行
        p = subprocess.Popen(self.worker_cmd, stdin=subprocess.PIPE)
        p.communicate(input=message)
        p.wait()

        return p.returncode != 0
