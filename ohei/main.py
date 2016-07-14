from __future__ import absolute_import

from ohei.datasource import BaseSource
from ohei.datasource import __sources__
from ohei.errors import DuplicatedPluginName
from ohei.errors import DuplicatedSourceName
from ohei.errors import NotAPlugin
from ohei.errors import NotASource
from ohei.plugins import BasePlugin
from ohei.plugins import __plugins__

_sources = __sources__
_plugins = __plugins__


def _register(s, store, exception):
    name = vars(s).get('__name__', s.__provide__)
    if name in store:
        raise exception(name, s)
    store.append(name)


def dep_count_array():
    return {n: len(p.__depends__) for n, p in _plugins.items()}


def src_count_array():
    return {n: len(p.__sources__) for n, p in _plugins.items()}


def register_source(s):
    if not issubclass(s, BaseSource):
        raise NotASource(s)
    _register(s, _sources, DuplicatedSourceName)


def remove_source(name):
    return _sources.pop(name)


def register_plugin(p):
    if not issubclass(p, BasePlugin):
        raise NotAPlugin(p)
    _register(p, _plugins, DuplicatedPluginName)


def remove_plugin(name):
    return _plugins.pop(name)
