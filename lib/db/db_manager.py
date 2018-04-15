# -*- coding: utf-8 -*-

"""
Db操作用クラス
with構文対応
"""
import json
import mysql.connector

class DbManager(object):

    def __init__(self):
        """ DB接続情報の読み込みを実行
        """
        self.processes = processes

    def __enter__(self):
        """ DB接続open処理
        """
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """ DB接続close処理
        """

    def connect(self, name):
        """ DB接続を実行

        :param name: string 接続先名称
        :return 接続オブジェクト
        """

    def close(self):
        """ DB接続を終了
        """

    def selectAll(self, sql, params=None):
        """ DB select sqlを実行し、全結果を返す

        :param sql: string 実行SQL文
        :param params: tuple 実行SQL文のパラメータ値(default:None)
        :return tuple SQL実行結果
        """

        return None

    def selectOne(self, sql, params=None):
        """ DB select sqlを実行し、一行目を返す

        :param sql: string 実行SQL文
        :param params: tuple 実行SQL文のパラメータ値(default:None)
        :return tuple SQL実行結果
        """

        return None

    def execuete(self, sql, params=None):
        """ DB insert/update/delete sqlを実行し、実行成功可否を返す

        :param sql: string 実行SQL文
        :param params: tuple 実行SQL文のパラメータ値(default:None)
        :return boolean SQL実行結果
        """

        return None

    def begin(self):
        """ DB トランザクション開始
        """

    def rollback(self):
        """ DB ロールバック
        """

    def commit(self):
        """ DB コミット
        """

    def __query(self, sql):
        """ DB sqlを実行

        :param sql: 実行SQL文
        """

    def close(self):
        """ DB 接続を閉じる
        """
