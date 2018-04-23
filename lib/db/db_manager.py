# -*- coding: utf-8 -*-

"""
Db操作用クラス
※実装参考
https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html
"""
import mysql.connector
from lib.configure import Configure

class DbManager(object):

    def __init__(self):
        """
        """

    def connect(self, name='default', option={}):
        """ DB接続を実行
        :param name:   string 接続名(default: 'default')
        :param option: dict   接続オプション(default:{})
        :return 接続オブジェクト
        """
        config = Configure.get('db.%s' % name)
        config.update(option)
        self.__connect = mysql.connector.connect(**config)
        return self

    def close(self):
        """ DB 接続を閉じる
        """
        self.cursor_close()
        self.__connect.close()

    def load_cursor(self):
        """ カーソルをロード(無い時は新たに作成)
        """
        if self.__cursor is None:
            self.__cursor = self.__connect.cursor(prepared=True)
        return self.__cursor

    def cursor_close(self):
        """ カーソルを閉じる
        """
        if not self.__cursor is None:
            self.__cursor.close()
        self.__cursor = None

    def select_all(self, sql, params=None, is_cursor_close=True):
        """ DB select sqlを実行し、全結果を返す
        @NOTE 変数にすべて取得データを格納するので、メモリオーバーフローに注意
        :param sql: string 実行SQL文
        :param params: tuple 実行SQL文のパラメータ値(default:None)
        :param is_cursor_close: カーソルをcloseするか(default:True)
        :return tuple SQL実行結果
        """
        # SQL文を実行
        self.__query(sql, params)
        records = self.load_cursor().fatchAll()
        if is_cursor_close:
            self.cursor_close()
        return records

    def select_one(self, sql, params=None, is_cursor_close=True):
        """ DB select sqlを実行し、一行目を返す
        :param sql: string 実行SQL文
        :param params: tuple 実行SQL文のパラメータ値(default:None)
        :param is_cursor_close: カーソルをcloseするか(default:True)
        :return tuple SQL実行結果
        """
        # SQL文を実行
        self.__query(sql, params)
        record = self.load_cursor().fatchOne()
        if is_cursor_close:
            self.cursor_close()
        return record

    def execute(self, sql, params=None):
        """ SQLを実行し、追加/変更したAUTOINCREMENTカラムの値を返す
        :param sql: string 実行SQL文
        :param params: tuple 実行SQL文のパラメータ値(default:None)
        :return mixed SQL実行結果
        """
        # SQL文を実行
        self.__query(sql, params)
        return self.load_cursor().lastrowid()

    def begin(self):
        """ DB トランザクションを貼る
        """
        self.__connect.start_transaction()

    def rollback(self):
        """ DB ロールバック
        """
        self.__connect.rollback()

    def commit(self):
        """ DB コミット
        """
        self.__connect.commit()

    def __query(self, sql, params):
        """ DB sqlを実行
        :param sql: 実行SQL文
        """
        self.load_cursor(prepared=True)
        self.__cursor.execute(sql, params)
