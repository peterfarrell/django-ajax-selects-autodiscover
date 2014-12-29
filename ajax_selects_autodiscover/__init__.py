def merge_dict(d1, d2):
    """
    Merges two dictionaries into one new dict using copy()

    :param d1: Dict()
    :param d2: Dict()
    :return: Dict()
    """
    merged = d1.copy()
    merged.update(d2)
    return merged


class AutoDiscover():

    def __getitem__(self, key):
        if not hasattr(self, 'channels'):
            self.channels = self.discover_channels()
        return self.channels[key]

    @staticmethod
    def discover_channels():
        from django.conf import settings
        from django.utils.importlib import import_module

        channels = {}

        for app in settings.INSTALLED_APPS:
            try:
                lookup = import_module('%s.lookup' % app)

                if hasattr(lookup, "AJAX_LOOKUP_CHANNELS"):
                    channels = merge_dict(channels, lookup.AJAX_LOOKUP_CHANNELS)
            except:
                pass

        return channels