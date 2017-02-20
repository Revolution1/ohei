import psutil
from ohei.plugins import BasePlugin


class Plugin(BasePlugin):
    __plugin_name__ = 'memory'
    __provide__ = 'memory'

    def get_value(self):
        data = {'ram': vars(psutil.virtual_memory()),
                'swap': vars(psutil.swap_memory())}
        return data
