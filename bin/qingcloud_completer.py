# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import os
from core import completer  # 整合

if __name__ == '__main__':
    # bash exports COMP_LINE and COMP_POINT, tcsh COMMAND_LINE only
    cline = os.environ.get('COMP_LINE') or os.environ.get('COMMAND_LINE') or ''
    cpoint = int(os.environ.get('COMP_POINT') or len(cline))
    completer.complete(cline, cpoint)