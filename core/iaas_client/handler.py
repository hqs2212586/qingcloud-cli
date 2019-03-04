# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from conf.iaas import constants as const


class IaasHandler(object):
    """处理iaas层云服务请求"""
    def __init__(self, connection=None):
        self.conn = connection

    def handle(self, action, directive):
        """根据操作将请求分派给指定的处理程序"""
        handler_map = {
            # instances
            const.ACTION_DESCRIBE_INSTANCES: self.conn.describe_instances,
            const.ACTION_RUN_INSTANCES: self.conn.run_instances,
            const.ACTION_START_INSTANCES: self.conn.start_instances,
            const.ACTION_STOP_INSTANCES: self.conn.stop_instances,
            const.ACTION_RESTART_INSTANCES: self.conn.restart_instances,
            const.ACTION_TERMINATE_INSTANCES: self.conn.terminate_instances,
            const.ACTION_RESIZE_INSTANCES: self.conn.resize_instances,
            const.ACTION_RESET_INSTANCES: self.conn.reset_instances,
            const.ACTION_MODIFY_INSTANCE_ATTRIBUTES: self.conn.modify_instance_attributes,
        }

