# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""项目最后打包发布到pypi仓库主要的配置信息"""

import os
import sys
import platform
from setuptools import setup, find_packages

config_sample = '''
qy_access_key_id: 'QINGCLOUDACCESSKEYID'
qy_secret_access_key: 'QINGCLOUDSECRETACCESSKEYEXAMPLE'
zone: 'ZONEID'
'''

def is_windows():
    return platform.system().lower() == 'windows'

def prepare_config_file():
    config_file = os.path.expanduser('~/.qingcloud/config.yaml')
    if os.path.exists(config_file):
        return

    d = os.path.dirname(config_file)
    if not os.path.exists(d):
        os.makedirs(d)

    with open(config_file, 'w') as fd:
        fd.write(config_sample)

def setup_qingcloud_completer():
    # only support linux
    if is_windows():
        return

    cmd = 'complete -C qingcloud_completer qingcloud'
    complete_file = '/etc/bash_completion.d/qingcloud-cli'
    complete_dir = os.path.dirname(complete_file)
    if os.path.exists(complete_dir) and os.access(complete_dir, os.W_OK):
        with open((complete_file), 'w') as fd:
            fd.write(cmd)
    else:
        with open(os.path.expanduser('~/.bash_profile'), 'a') as fd:
            fd.write('\n\n# QingCloud CLI\n%s\n' % cmd)


if len(sys.argv) < 2 or sys.argv[1] != 'install':
    bin_scripts = ['bin/qingcloud', 'bin/qingcloud.cmd', 'bin/qingcloud_completer']
elif is_windows():
    bin_scripts = ['bin/qingcloud.cmd']
else:
    bin_scripts = ['bin/qingcloud', 'bin/qingcloud_completer']

setup(
    name = 'qingcloud-cli',   # 包名
    version = '0.0.1',        # 当前包版本
    description = 'Command Line Interface for QingCloud.',
    long_description = open('README.rst', 'rb').read().decode('utf-8'),
    keywords = 'qingcloud iaas qingstor cli',
    author = 'Yunify Team',
    author_email = 'simon@yunify.com',
    url = 'https://docs.qingcloud.com',   # 包的项目地址
    scripts=bin_scripts,
    packages = find_packages('.'),  # 包含的包
    package_dir = {'qingcloud-cli': 'qingcloud'},
    namespace_packages = ['qingcloud'],
    include_package_data = True,
    install_requires = [    # 模块所依赖的python模块
        'argparse>=1.1',
        'PyYAML>=3.1',
    ],
    License="Apache License 2.0",    # 授权方式
    classifiers=[
        'Environment :: CLI Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)

if len(sys.argv) >= 2 and sys.argv[1] == 'install':
    prepare_config_file()
    setup_qingcloud_completer()
