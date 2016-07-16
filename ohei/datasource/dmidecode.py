from __future__ import absolute_import

from ohei.datasource import BaseSource
from ohei.utils.command import exec_cmd
from ohei.utils.dmidecode import parse_dmi


class Source(BaseSource):
    __provide__ = 'dmidecode'

    def get_data(self):
        try:
            dmidecode = exec_cmd('dmidecode')
            return parse_dmi(dmidecode)
        except Exception:
            return ''
