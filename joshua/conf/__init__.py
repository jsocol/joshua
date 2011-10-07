import os
import imp

import default_settings


ENVIRONMENT_VARIABLE = 'JOSHUA_SETTINGS'


class Settings(object):
    def __init__(self, settings_module):
        self._settings = settings_module

    def __getattr__(self, attr):
        env_var = 'JOSHUA_%s' % attr
        if env_var in os.environ:
            val = os.environ[env_var]
        if hasattr(self._settings, attr):
            val = getattr(self._settings, attr)
        else:
            val = getattr(default_settings, attr)
        # Save for later.
        setattr(self, attr, val)
        return val

    def configure(self, **options):
        for o in options:
            setattr(self, o, options[o])


if ENVIRONMENT_VARIABLE in os.environ:
    try:
        settings_module = os.environ[ENVIRONMENT_VARIABLE]
        if not settings_module:  # Defined but empty.
            raise KeyError
    except KeyError:
        raise ImportError('Settings cannot be imported, because %s is '
                          'undefined.' % ENVIRONMENT_VARIABLE)
else:
    settings_module = 'settings'

find = imp.find_module(settings_module, ['.', '..'])
mod = imp.load_module(settings_module, *find)
settings = Settings(mod)
