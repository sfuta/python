# -*- coding: utf-8 -*-

"""
AWS Simple Queue Serviceのクライアントクラス
with構文対応
"""
import json

class SqsClient(object):

    def __init__(self):
        """ SQS接続情報の読み込みを実行
        """
        self.processes = processes

    def __enter__(self):
        """ SQS接続open処理
        """
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """ SQS接続close処理
        """

    def connect(self, name):
        """ SQS接続を実行

        :param name: string 接続先名称
        :return 接続オブジェクト
        """

    def close(self):
        """ SQS接続を終了
        """

    def push(self, item):
        """ SQSに指定した値を格納
            ->格納する値はjson encode後にgzcompresssした値

        :param item: mixed 格納する値
        :return boolean 成功可否
        """

    def pop(self):
        """ SQSから値を取得

        :param item: mixed 格納する値
        :return list 格納していた値
        """
