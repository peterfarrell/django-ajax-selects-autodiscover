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


def autodiscover():
    """
    Auto-discover INSTALLED_APPS admin.py modules and fail silently when
    not present. This forces an import on them to register any admin bits they
    may want.
    """

    from django.conf import settings
    from django.utils.importlib import import_module

    channels = {}

    for app in settings.INSTALLED_APPS:
        lookup = import_module('%s.lookup' % app)

        if 'AJAX_LOOKUP_CHANNELS' in lookup:
            merge_dict(channels, lookup.AJAX_LOOKUP_CHANNELS)

    return channels