# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


from core.iaas_client.actions import instance

class ActionManager(object):
    @classmethod
    def get_action(cls, action):
        return cls.action_table.get(action)

    @classmethod
    def get_valid_actions(cls):
        return sorted(ActionManager.action_table.keys())

    action_table = {
        ## instance ##
        'run-instances': instance.RunInstancesAction,
        'describe-instances': instance.DescribeInstancesAction,
        'terminate-instances': instance.TerminateInstancesAction,
    }