# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


"""
项目的单元测试文件
"""
import unittest
import core.utils.host as host


class TestHost(unittest.TestCase):
    def test_ip(self):
        self.assertIsNotNone(host.ip())

    def test_name(self):
        self.assertIsNotNone(host.name())


if __name__ == '__main__':
    unittest.main()