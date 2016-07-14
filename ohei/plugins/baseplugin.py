class BasePlugin(object):
    __plugin_name__ = ''
    __provide__ = ''
    __sources__ = []
    __depends__ = []

    def __init__(self, source, results):
        self._source = source
        self._depend = results

    def get_source(self, name):
        return self._source.get(name)

    def get_depend(self, name):
        return self._depend.get(name)

    def get_value(self):
        raise NotImplementedError()
