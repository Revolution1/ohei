"""
The reason we need this file is that:
when we run ohei in a container, we can mount host's dirs into the container
and set these environment variables so we can still get the information we need.
"""

from os import getenv as _e

from os.path import join as _j


class DIRS(object):
    ROOT = _e('DIR_ROOT', '/')
    ETC = _e('DIR_ETC', _j(ROOT, '/etc'))
    PROC = _e('DIR_PROC', _j(ROOT, '/proc'))
    USR = _e('DIR_USR', _j(ROOT, '/usr'))
    USR_LOCAL = _e('DIR_USR_LOCAL', _j(USR, '/local'))
    VAR = _e('DIR_VAR', _j(ROOT, '/var'))
    VAR_RUN = _e('DIR_VAR_RUN', _j(VAR, '/run'))
    HOME = _e('DIR_HOME', _e('HOME', _j(ROOT, '/home')))


CPU_PERCENT_INTERVAL = float(_e('CPU_PERCENT_INTERVAL', 0.1))
