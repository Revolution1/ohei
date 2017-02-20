DUPLICATED_SOURCE_NAME = 'duplicated_source_name'
DUPLICATED_PLUGIN_NAME = 'duplicated_plugin_name'


class DuplicatedName(Exception):
    type = ''
    message = ''

    def __init__(self, name, module):
        super(DuplicatedName, self).__init__(self.message)
        self.name = name
        self.module = module

    def __str__(self):
        return 'There is already a %s named %s exist. Please check you module : %s' % \
               (self.type, self.name, self.module)


class DuplicatedSourceName(DuplicatedName):
    message = DUPLICATED_SOURCE_NAME

    def __init__(self, name, module):
        super(DuplicatedSourceName, self).__init__(name, module)


class DuplicatedPluginName(DuplicatedName):
    message = DUPLICATED_PLUGIN_NAME

    def __init__(self, name, module):
        super(DuplicatedPluginName, self).__init__(name, module)


class NotAPlugin(Exception):
    def __str__(self):
        return 'Not a plugin: %s.' % self.message


class NotASource(Exception):
    def __str__(self):
        return 'Not a Source: %s.' % self.message


class SourceNotExist(Exception):
    def __init__(self, plugin, source):
        self.plugin = plugin
        self.source = source

    def __str__(self):
        return 'Required source not exist. Plugin: %s, Source: %s.' % \
               (self.plugin, self.source)
