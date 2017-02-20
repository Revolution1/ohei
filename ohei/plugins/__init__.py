from __future__ import absolute_import

import glob
from importlib import import_module

import os
from ohei.errors import DuplicatedPluginName
from ohei.plugins.baseplugin import BasePlugin


def _get_plugins():
    path = os.path.dirname(__file__)
    pys = glob.glob(os.path.join(path, '*.py'))
    pys.remove(os.path.join(path, '__init__.py'))
    pys.remove(os.path.join(path, 'baseplugin.py'))
    modules = [i[len(path) + 1:-3] for i in pys]
    _names = []
    plugins = {}
    for i in modules:
        m = import_module('ohei.plugins.%s' % i)
        name = m.Plugin.__plugin_name__
        plugin = m.Plugin
        if name in _names:
            raise DuplicatedPluginName(name, m)
        _names.append(name)
        plugins[name] = plugin
    return plugins


__plugins__ = _get_plugins()
