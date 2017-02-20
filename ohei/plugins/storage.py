from ohei.plugins import BasePlugin


class Plugin(BasePlugin):
    __plugin_name__ = 'storage'
    __provide__ = 'storage'

    def get_value(self):
        data = {}
        return data
