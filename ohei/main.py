from __future__ import absolute_import

from ohei.datasource import BaseSource
from ohei.datasource import __sources__
from ohei.errors import DuplicatedPluginName, SourceNotExist
from ohei.errors import DuplicatedSourceName
from ohei.errors import NotAPlugin
from ohei.errors import NotASource
from ohei.plugins import BasePlugin
from ohei.plugins import __plugins__


class Ohei(object):
    def __init__(self):
        self._sources = __sources__
        self._plugins = __plugins__

    def _register(self, s, store, exception):
        name = vars(s).get('__name__', s.__provide__)
        if name in store:
            raise exception(name, s)
        store.append(name)

    def register_source(self, s):
        if not issubclass(s, BaseSource):
            raise NotASource(s)
        self._register(s, self._sources, DuplicatedSourceName)

    def remove_plugin(self, name):
        return self._plugins.pop(name)

    def remove_source(self, name):
        return self._sources.pop(name)

    def register_plugin(self, p):
        if not issubclass(p, BasePlugin):
            raise NotAPlugin(p)
        self._register(p, self._plugins, DuplicatedPluginName)

    def _dep_count_array(self):
        return {n: (set(p.__depends__), p) for n, p in self._plugins.items()}

    def _src_count_array(self, ):
        return {n: (set(p.__sources__), p) for n, p in self._plugins.items()}

    def _bake_source(self, s):
        source = s()
        return source.get_data()

    def _run_plugin(self, p, source, results):
        plugin = p(source, results)
        return plugin.get_value()

    def run(self):
        srcs_ary = self._src_count_array()
        deps_ary = self._dep_count_array()
        sources = {}
        results = {}
        for n, s in self._sources.items():
            sources[n] = self._bake_source(s)
            for name, (srcs, plugin) in srcs_ary.items():
                if n in srcs:
                    srcs.remove(n)
        for name, (srcs, plugin) in srcs_ary.items():
            if srcs:
                raise SourceNotExist(name, srcs)
        while deps_ary:
            for name, (deps, plugin) in deps_ary.items():
                if not deps:
                    results[name] = self._run_plugin(plugin, sources, results)
                    deps_ary.pop(name)
                    for n, (d, p) in deps_ary.items():
                        if name in d:
                            d.remove(name)
        return results


if __name__ == '__main__':
    import json

    ohei = Ohei()
    print(json.dumps(ohei.run(), indent=4))
