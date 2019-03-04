# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import os
import logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INDENT = ' ' * 2
NEWLINE = '\n' + ' ' * 2
SERVICES = ('iaas', 'qs')  # 两种服务


Params = {
    "name": "qingcloud",
    "description": "Command Line Interface for QingCloud.",
    "detail_description": open("%s/docs/README.rst" % BASE_DIR, 'rb').read().decode('utf-8'),
    "port":8000,
    'request_timeout':30,
    "urls":{
        "asset_report_with_no_id":"/asset/report/asset_with_no_asset_id/",  # 新资产批准区接口
        "asset_report":"/asset/report/",   # 正式资产表接口
    },
    'asset_id': '%s/var/.asset_id' % BASE_DIR,  # 本机收集的数据保存在本地隐藏文件中
    'log_file': '%s/logs/run_log' % BASE_DIR,

    'auth':{
        'user':'lijie3721@126.com',
        'token': 'abc'
    },
}

# 日志
LOG_LEVEL = logging.INFO

LOG_TYPES = {
    "run": "run.log",
    "error": "error.log"
}

LOG_PATH = os.path.join(BASE_DIR, "log")

LOG_FORMAT = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")