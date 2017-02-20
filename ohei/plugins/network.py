from ohei.plugins import BasePlugin


class Plugin(BasePlugin):
    __plugin_name__ = 'network'
    __provide__ = 'network'

    def get_value(self):
        data = {}
        return data
