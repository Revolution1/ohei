import psutil
from ohei.consts import DIRS
from ohei.plugins import BasePlugin
from ohei.utils.hwinfo.host import cpuinfo


class Plugin(BasePlugin):
    __plugin_name__ = 'cpu'
    __provide__ = 'cpu'
    __sources__ = ['dmidecode']

    def get_value(self):
        data = {}
        data.update(self._cpu_solid())
        data.update(self._cpu_runtime())
        return data

    def _cpu_runtime(self):
        per = psutil.cpu_percent(percpu=True)
        avg = sum(per) / len(per)
        return {
            'percent': {
                'average': per,
                'per_cpu': avg
            }
        }

    def _get_cpuinfo(self):
        with open('{proc}/cpuinfo'.format(proc=DIRS.PROC), 'r') as f:
            info = f.read()
            return cpuinfo.CPUInfoParser(info).parse_items()

    def _cpu_solid(self):
        ps = self._get_cpuinfo()
        pc = psutil.cpu_count(logical=False)
        lc = psutil.cpu_count()
        dmi = self.get_source('dmidecode')
        cpus = 0
        for type, content in dmi:
            if type == 4:
                if content.get('Status') == 'Populated, Enabled':
                    cpus += 1
        return {
            'processors': ps,
            'physical_cores': pc,
            'logical_cores': lc,
            'hyper_thread': lc > pc,
            'cpus': cpus or 1,
        }


if __name__ == '__main__':
    plugin = Plugin({}, {})
    print(plugin.get_value())
