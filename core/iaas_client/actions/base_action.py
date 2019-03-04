# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


import sys
from optparse import OptionParser
from core.conn import APIConnection
from core.iaas_client.handler import IaasHandler
from core.utils import load_conf, send_request, get_expire_time

class BaseAction(object):
    action = ''
    command = ''
    usage = ''
    description = ''

    @classmethod
    def get_argument_parser(cls):            #
        parser = OptionParser(
            prog='qingcloud iaas %s' % cls.command,
            usage=cls.usage,
            description=cls.description
        )
        cls.add_common_arguments(parser)
        cls.add_ext_arguments(parser)
        return parser

    @classmethod
    def add_common_arguments(cls, parser):    # 添加共同参数
        pass

    @classmethod
    def add_ext_arguments(cls, parser):
        pass

    @classmethod
    def build_directive(cls, options):
        return None

    @classmethod
    def main(cls, args):
        parser = cls.get_argument_parser()
        options = parser.parse_args(args)

        directive = cls.build_directive(options)
        if directive is None:
            parser.print_help()
            sys.exit(-1)

        # 加载配置文件
        conf = load_conf(options.conf_file)
        if conf is None:
            sys.exit(-1)
        conf['expires'] = get_expire_time()

        if options.zone:
            conf.update(zone=options.zone)

        # 发送请求
        connection = APIConnection(**conf)
        handler = IaasHandler(connection)
        return send_request(cls.action, directive, handler)