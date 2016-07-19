"""Module for parsing the output of /proc/cpuinfo"""

from ..util import CommandParser

REGEX_TEMPLATE = r'%s([\ \t])+\:\ (?P<%s>.*)'


class CPUInfoParser(CommandParser):
    ITEM_SEPERATOR = "\n\n"

    ITEM_REGEXS = [
        REGEX_TEMPLATE % ('processor', 'processor'),
        REGEX_TEMPLATE % ('vendor_id', 'vendor_id'),
        REGEX_TEMPLATE % ('cpu\ family', 'cpu_family'),
        REGEX_TEMPLATE % ('model', 'model'),
        REGEX_TEMPLATE % ('model\ name', 'model_name'),
        REGEX_TEMPLATE % ('stepping', 'stepping'),
        REGEX_TEMPLATE % ('microcode', 'microcode'),
        REGEX_TEMPLATE % ('cpu\ MHz', 'cpu_MHz'),
        REGEX_TEMPLATE % ('cache\ size', 'cache_size'),
        REGEX_TEMPLATE % ('physical\ id', 'physical_id'),
        REGEX_TEMPLATE % ('siblings', 'siblings'),
        REGEX_TEMPLATE % ('core\ id', 'core_id'),
        REGEX_TEMPLATE % ('cpu\ cores', 'cpu_cores'),
        REGEX_TEMPLATE % ('apicid', 'apicid'),
        REGEX_TEMPLATE % ('initial\ apicid', 'initial_apicid'),
        REGEX_TEMPLATE % ('fpu', 'fpu'),
        REGEX_TEMPLATE % ('fpu_exception', 'fpu_exception'),
        REGEX_TEMPLATE % ('cpuid\ level', 'cpuid_level'),
        REGEX_TEMPLATE % ('wp', 'wp'),
        REGEX_TEMPLATE % ('flags', 'flags'),
        REGEX_TEMPLATE % ('bogomips', 'bogomips'),
        REGEX_TEMPLATE % ('clflush\ size', 'clflush_size'),
        REGEX_TEMPLATE % ('cache_alignment', 'cache_alignment'),
        REGEX_TEMPLATE % ('address\ sizes', 'address_sizes')
    ]
