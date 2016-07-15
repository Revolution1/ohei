from __future__ import absolute_import

from ohei.datasource import BaseSource
from ohei.datasource import __sources__
from ohei.errors import DuplicatedPluginName, SourceNotExist
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


def register_source(s):
    if not issubclass(s, BaseSource):
        raise NotASource(s)
    _register(s, _sources, DuplicatedSourceName)


def remove_plugin(name):
    return _plugins.pop(name)


def remove_source(name):
    return _sources.pop(name)


def register_plugin(p):
    if not issubclass(p, BasePlugin):
        raise NotAPlugin(p)
    _register(p, _plugins, DuplicatedPluginName)


def _dep_count_array():
    return {n: (set(p.__depends__), p) for n, p in _plugins.items()}


def _src_count_array():
    return {n: (set(p.__sources__), p) for n, p in _plugins.items()}


def _bake_source(s):
    source = s()
    return source.get_data()


def _run_plugin(p, source, results):
    plugin = p(source, results)
    return plugin.get_value()


def run():
    srcs_ary = _src_count_array()
    deps_ary = _dep_count_array()
    sources = {}
    results = {}
    for n, s in _sources.items():
        sources[n] = _bake_source(s)
        for name, (srcs, plugin) in srcs_ary.items():
            if n in srcs:
                srcs.pop(n)
    for name, (srcs, plugin) in srcs_ary.items():
        if srcs:
            raise SourceNotExist(name, srcs)
    while deps_ary:
        for name, (deps, plugin) in deps_ary.items():
            if not deps:
                results[name] = _run_plugin(plugin, sources, results)
                deps_ary.pop(name)
                for n, (d, p) in deps_ary.items():
                    if name in d:
                        d.remove(name)
    return results


if __name__ == '__main__':
    print(run())
