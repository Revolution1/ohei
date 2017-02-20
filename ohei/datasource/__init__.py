from __future__ import absolute_import

import glob
from importlib import import_module

import os
from ohei.datasource.basesource import BaseSource
from ohei.errors import DuplicatedSourceName


def _get_sources():
    path = os.path.dirname(__file__)
    pys = glob.glob(os.path.join(path, '*.py'))
    pys.remove(os.path.join(path, '__init__.py'))
    pys.remove(os.path.join(path, 'basesource.py'))
    modules = [i[len(path) + 1:-3] for i in pys]
    _names = []
    sources = {}
    for i in modules:
        m = import_module('ohei.datasource.%s' % i)
        name = m.Source.__provide__
        source = m.Source
        if name in _names:
            raise DuplicatedSourceName(name, m)
        _names.append(name)
        sources[name] = source
    return sources


__sources__ = _get_sources()
