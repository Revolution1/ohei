from ohei.consts import DIRS
from ohei.plugins import BasePlugin
from ohei.utils.hwinfo.host import cpuinfo


class Plugin(BasePlugin):
    __plugin_name__ = 'cpu'
    __provide__ = 'cpu'
    __sources__ = ['dmidecode']

    def get_value(self):
        data = {}
        data.update(self._cpu_runtime())
        data.update(self._solid)  # put calculate process into _cpu_runtime() to save time
        return data

    def _get_stat(self):
        with open('{proc}/stat'.format(proc=DIRS.PROC), 'r') as f:
            stat = []
            for line in f.readlines():
                if line.startswith('cpu'):
                    split = line.split()
                    stat.append((split[0], sum([int(i) for i in split[1:]]), int(split[4])))
            return stat

    def _cpu_runtime(self):
        stat1 = self._get_stat()
        self._solid = self._cpu_solid()  # do something instead of using time.sleep
        stat2 = self._get_stat()
        result = {}
        for name, total, idle in zip(stat1, stat2):
            result[name[0]] = 1 - (idle[1] - idle[0]) / float(total[1] - total[0])
        return {
            'percent': {
                'average': result.pop('cpu'),
                'per_cpu': result
            }
        }

    def _get_cpuinfo(self):
        with open('{proc}/cpuinfo'.format(proc=DIRS.PROC), 'r') as f:
            info = f.read()
            return cpuinfo.CPUInfoParser(info).parse_items()

    def _cpu_solid(self):
        info = self._get_cpuinfo()
        core_ids = set()
        physical_ids = set()
        logical_cores = len(info)
        for c in info:
            core_ids.add(c['core_id'])
            physical_ids.add(c['physical_id'])
        dmi = self.get_source('dmidecode')
        cpus = 0
        for type, content in dmi:
            if type == 4:
                if content.get('Status') == 'Populated, Enabled':
                    cpus += 1
        return {
            'processors': len(physical_ids),
            'physical_cores': len(core_ids),
            'logical_cores': logical_cores,
            'hyper_threading': logical_cores > len(physical_ids),
            'cpus': cpus or 1,
        }
