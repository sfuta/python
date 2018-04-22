# -*- coding: utf-8 -*-

"""
AWS Simple Queue Serviceのクライアントクラス
"""
import boto3
from lib.configure import Configure

class SqsClient(object):

    def __init__(self, queue_name):
        """ SQS接続情報の読み込みを実行
        :param queue_name: string キュー名(設定ファイルから取得)
        """
        # 指定のキュー名より、設定ファイルからキューのURLを取得
        self.queue_url = Configure.get('sqs.' + queue_name + '.url')
        # クライアントを設定
        self.client = boto3.client('sqs',
            aws_access_key_id = Configure.get('aws.access_key'),
            aws_secret_access_key = Configure.get('aws.secret_key'),
            region_name = Configure.get('aws.region')
        )

    def pop(self, wait_time = 20, visible_time = 10):
        """ SQSから値を取得
        :param wait_time int 待ち時間(sec)：1〜20sec(default:20)
        :param visible_time int 可視時間(sec)：他Sessionが取得可となるまでの時間(default:10sec)
        :return string 取得値
        """
        try:
            res = client.receive_message(
                QueueUrl = self.queue_url,
                MaxNumberOfMessages = 1, MessageAttributeNames = ['All'],
                WaitTimeSeconds = wait_time, VisibilityTimeout = visible_time
            )
        except Exception as e:
            # @TODO error 処理
            print('ERROR:' + str(e))

        if not 'Messages' in res.keys():
            return ""

        msg = res['Messages'][0]
        # msg取得成功後は多重取得回避のため、削除
        self.client.delete_message(
            QueueUrl = self.queue_url, ReceiptHandle = msg['ReceiptHandle']
        )
        return msg['Body']

        try:
            response = sqs.receive_message(
                QueueUrl=url,
            )

        return response

    def push(self, item):
        """ SQSに指定した値を格納
            ->格納する値はjson encode後にgzcompresssした値

        :param item: mixed 格納する値
        :return boolean 成功可否
        """
        # 未対応
