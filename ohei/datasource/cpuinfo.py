from __future__ import absolute_import

from ohei.consts import DIRS
from ohei.datasource import BaseSource


class Source(BaseSource):
    __provide__ = 'cpuinfo'

    def get_data(self):
        with open('{proc}/cpuinfo'.format(proc=DIRS.PROC)) as f:
            return f.read()
