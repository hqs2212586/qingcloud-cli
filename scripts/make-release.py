# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
    make-release
    ~~~~~~~~~~~~
    Helper script that performs a release.  Does pretty much everything
    automatically for us.
    
    make-release文件用来自动控制版本。通过Git 的提交记录了来作为项目的唯一版本号标识，
    再对 init 文件进行重新写入达到持续集成时版本号自增的目的。
    :copyright: (c) 2019 by hqs.
"""
import re
import sys
from subprocess import Popen, PIPE


def set_filename_version(filename, version_number, pattern):
    changed = []

    def inject_version(match):
        before, old, after = match.groups()
        changed.append(True)
        return before + version_number + after

    with open(filename) as f:
        contents = re.sub(r"^(\s*%s\s*=\s*')(.+?)(')" % pattern,
                          inject_version, f.read(),
                          flags=re.DOTALL | re.MULTILINE)

    if not changed:
        fail('Could not find %s in %s', pattern, filename)

    with open(filename, 'w') as f:
        f.write(contents)


def set_init_version(version):
    info('Setting __init__.py version to %s', version)
    set_filename_version('proxy/__init__.py', version, '__version__')


def fail(message, *args):
    print(sys.stderr, 'Error:', message % args)
    sys.exit(1)


def info(message, *args):
    print(sys.stderr, message % args)


def main():
    describe = 'git rev-list --count HEAD'
    version = Popen(describe.split(), stdout=PIPE).communicate()[0].strip()
    set_init_version(version)


if __name__ == '__main__':
    main()