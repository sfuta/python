# -*- coding: utf-8 -*-

"""
Api操作用クラス
with構文対応
※実装参考
https://qiita.com/hoto17296/items/8fcf55cc6cd823a18217
"""
import json
import urllib.request

class Client(object):

    def __init__(self):
        """ Api接続情報の読み込みを実行
        """
        self.processes = processes

    def __enter__(self):
        """ Api接続open処理
        """
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """ Api接続close処理
        """

    def open(self, name):
        """ Api接続を実行

        :param name: string 接続先名称
        :return 接続オブジェクト
        """

    def close(self):
        """ Api接続を終了
        """

    def get(self, params=None):
        """ Api requestを投げ結果の取得を実行

        :param params: hash APIのパラメータを指定
        :return list api実行結果(json decodeした値)
        """

        return None
