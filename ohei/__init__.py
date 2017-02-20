import sys

import os

_path = os.path.dirname(__file__)
_path = os.path.abspath(os.path.join(_path, os.pardir))
sys.path.append(_path)

from ohei.__main__ import Ohei
from ohei.consts import DIRS
import psutil

# patch psutil
psutil.PROCFS_PATH = DIRS.PROC
