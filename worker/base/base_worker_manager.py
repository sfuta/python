# -*- coding: utf-8 -*-

"""
worker管理基底クラス
"""

class BaseWorkerManager(object):

    def __init__(self):
        """ 利用クラスのインスタンス化等
        """

    def before(self):
        """ 開始処理を記載
        """
        print "BaseWorker"

    def after(self):
        """ 完了後処理を記載
        """

    def run(self):
        """ 実行処理を記載
        """

        return None
