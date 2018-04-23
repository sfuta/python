# -*- coding: utf-8 -*-

"""
Api操作用クラス
※サンプルURL:https://jsonplaceholder.typicode.com/
"""

import json
import urllib
import urllib2

class Client(object):

    def __init__(self, url):
        """ Api接続情報の読み込みを実行
        :param url: string 接続先URL
        """
        self.__url = url

    def get(self, params={}):
        """ Api接続を実行
        :param params: dict 接続先のパラメータ
        :return string response文字列
        """
        querystring = ("?" if params != {} else "") + urllib.urlencode(params)
        try:
            response = urllib2.urlopen(self.__url + querystring)
            return response.read()
        except urllib2.HTTPError as e:
            # @TODO エラー処理の記載
            print 'Error code: ', e.code
        except urllib2.URLError as e:
            # @TODO エラー処理の記載
            print 'Reason: ', e.reason

# if __name__ == '__main__':
#     c = Client('https://jsonplaceholder.typicode.com/posts')
#     print c.get({'userId':2})
