# -*- coding: utf-8 -*-

import yaml

class Configure(object):
    """ 設定ファイルの値を管理するためのクラス
    """
    __config_dict = {}

    def __init__(self):
        print "Configure class is not init.(all static method)"

    @staticmethod
    def load_yaml(path):
        """ yaml形式の設定ファイル読み込みを実行
        :param path: string 読み込みファイルパス
        """
        # 設定ファイル内容をマージする
        with open(path) as file:
            Configure.__config_dict.update(yaml.load(file))

    @staticmethod
    def get(key):
        """ キーに該当する設定ファイルの値を取得
        :param key: string 設定値取得キー
        """
        def __get(k, v):
            if '.' in k:
                _k = k[k.find('.')+1:]
                _v = v[k.split('.')[0]]
                return __get(_k, _v)
            return v[k]

        return __get(key, Configure.__config_dict)
