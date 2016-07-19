import time

from ohei.consts import CPU_PERCENT_INTERVAL
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
        data.update(self._cpu_solid())
        return data

    def _get_stat(self):
        with open('{proc}/stat'.format(proc=DIRS.PROC), 'r') as f:
            stat = []
            for line in f.readlines():
                if line.startswith('cpu'):
                    split = line.split()
                    stat.append((split[0], sum([int(i) for i in split[1:]]), int(split[4])))  # name,total,idle
            return stat

    def _cpu_runtime(self):
        def calculate(total1, idle1, total2, idle2):
            t1_busy = total1 - idle1
            t2_busy = total2 - idle2
            # this usually indicates a float precision issue
            if t2_busy <= t1_busy:
                return 0.0
            busy_delta = t2_busy - t1_busy
            all_delta = total2 - total1
            busy_per = (busy_delta / all_delta) * 100
            return round(busy_per, 1)

        stat1 = self._get_stat()
        time.sleep(CPU_PERCENT_INTERVAL)
        stat2 = self._get_stat()
        result = {}
        for (name, total1, idle1), (_, total2, idle2) in zip(stat1, stat2):
            result[name] = calculate(total1, idle1, total2, idle2)
        result.pop('cpu')
        return {
            'percent': {
                # 'average': result.pop('cpu'),
                'average': sum(result.values()) / len(result),
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
        return {
            'cpus': len(physical_ids),
            'physical_cores': len(core_ids),
            'logical_cores': logical_cores,
            'hyper_threading': logical_cores > len(core_ids),
        }
