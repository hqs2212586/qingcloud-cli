# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import optparse
import pkg_resources
import sys, os, json, datetime
from difflib import get_close_matches
from conf import settings
from core import api_token

from core.iaas_client.actions import ActionManager as IaaSActionManager


class ArgvHandler(object):
    def __init__(self, argv_list):
        self.args = argv_list
        self.parse_argv()


    def parse_argv(self):   # 检查参数
        if len(self.args) < 2:   # 如果参数小于两个
            self.invalid_service_cause_exit()

        if self.args[1].lower() in ('--version', '-v'):  # 如果第一个参数是-v
            version = pkg_resources.require("qingcloud-cli")[0].version
            print('qingcloud-cli version %s' % version)
            sys.exit(0)

        service = self.args[1]

        if service not in settings.SERVICES:
            suggest_services = get_close_matches(service, settings.SERVICES)
            self.invalid_service_cause_exit(suggest_services)

        if len(self.args) < 3:
            self.invalid_action_cause_exit(service)    # 无效操作退出

        valid_actions = self.get_valid_actions(service)


    @staticmethod
    def invalid_service_cause_exit(suggest_services=None):   # 无效服务退出
        usage = settings.INDENT + '%(prog)s <service> <action> [parameters]\n\n' \
                + 'Here are valid services:\n\n' \
                + settings.INDENT + settings.NEWLINE.join(settings.SERVICES)

        if suggest_services:
            usage += '\n\nInvalid service, maybe you meant:\n  ' \
                     + ','.join(suggest_services)

        parser = optparse.OptionParser(
            prog='qingcloud',
            usage=usage,
        )
        parser.print_help()
        sys.exit(-1)

    def invalid_action_cause_exit(self, service, suggest_actions=None):    # 无效操作退出
        usage = settings.NEWLINE + '%(prog)s <action> [parameters]\n\n' \
                + 'Here are valid actions:\n\n' \
                + settings.INDENT + settings.NEWLINE.join(self.get_valid_actions(service))

        if suggest_actions:
            usage += '\n\nInvalid action, maybe you meant:\n  ' \
                     + settings.NEWLINE.join(suggest_actions)

        parser = optparse.OptionParser(
            prog='qingcloud %s' % service,
            usage=usage,
        )
        parser.print_help()
        sys.exit(-1)

    @staticmethod
    def get_valid_actions(service):  # 有效操作
        if service == 'iaas':
            return IaaSActionManager.get_valid_actions()
        elif service == 'qs':
            pass

    @staticmethod
    def get_action(service, action):
        if service == 'iaas':
            return IaaSActionManager.get_action(action)
        elif service == 'qs':
            pass

    def __attach_token(self,url_str):
        '''
        通过token和用户名生成md5，添加到url请求中
        generate md5 by token_id and username,and attach it on the url request
        :param url_str: post请求地址
        :return:
        '''
        user = settings.Params['auth']['user']
        token_id = settings.Params['auth']['token']

        md5_token,timestamp = api_token.get_token(user,token_id)  # 生成md5和时间戳：/MadkingClint/core/api_token
        url_arg_str = "user=%s&timestamp=%s&token=%s" %(user,timestamp,md5_token)  # 将用户名、时间戳、token信息拼接
        if "?" in url_str:   # 说明本来url就有参数，可以直接在后面用&拼接请求
            new_url = url_str + "&" + url_arg_str
        else:      # 没有问号说明本身没有参数，需要拼接'?'
            new_url = url_str + "?" + url_arg_str
        return  new_url
        #print(url_arg_str)



    def log_record(self, log, action_type=None):
        f = open(settings.Params["log_file"],"ab")
        if log is str:
            pass
        if type(log) is dict:
            if "info" in log:
                for msg in log["info"]:
                    log_format = "%s\tINFO\t%s\n" %(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),msg)
                    #print msg
                    f.write(log_format.encode())
            if "error" in log:
                for msg in log["error"]:
                    log_format = "%s\tERROR\t%s\n" %(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),msg)
                    f.write(log_format.encode())
            if "warning" in log:
                for msg in log["warning"]:
                    log_format = "%s\tWARNING\t%s\n" %(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),msg)
                    f.write(log_format.encode())

        f.close()


def main():
    # sys.argv：命令行参数List,第一个元素是程序本身路径
    args = sys.argv
    print(args)
    cli = ArgvHandler(args)  # 传递sys.argv参数给ArgvHandler类
    action = cli.get_action(args[1], args[2])
    action.main(args[3:])