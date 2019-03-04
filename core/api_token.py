# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


import hashlib,time


def get_token(username,token_id):
    """
    生成md5和时间戳
    :param username: settings.Params['auth']['user']
    :param token_id: settings.Params['auth']['token']
    :return:
    """
    timestamp = int(time.time())   # 根据时间动态生成时间戳
    md5_format_str = "%s\n%s\n%s" %(username,timestamp,token_id)   # 拼接字符串
    obj = hashlib.md5()
    obj.update(md5_format_str.encode())  # 对字符串做hash
    print("token format:[%s]" % md5_format_str)
    print("token :[%s]" % obj.hexdigest())   # token :[dec365f76143db8e889d0f819317d0d6]
    return obj.hexdigest()[10:17], timestamp   # 截取部分md5值和时间戳 eg.('43db8e8', 1548049321)


if __name__ =='__main__':
    print(get_token('alex','test'))