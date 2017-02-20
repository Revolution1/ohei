from ohei.plugins import BasePlugin


class Plugin(BasePlugin):
    __plugin_name__ = 'virtualization'
    __provide__ = 'virtualization'

    def get_value(self):
        data = {}
        return data
