#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

""" workermanager系実行スクリプト
"""

# クラスのメタ情報取得
task_name   = sys.argv[1]
class_name  = task_name + "WorkerManager"
dir_name    = re.sub("([A-Z])", lambda x:"_" + x.group(1).lower(), task_name)[1:]
module_name = dir_name + "." + dir_name + "_worker_manager"

# メタ情報からインスタンス作成
module = __import__(module_name, fromlist=[class_name])
worker_manager = getattr(module, class_name)
wm = worker_manager()

# 実処理記載
wm.before()
