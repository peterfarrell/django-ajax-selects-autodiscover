django-ajax-selects-autodiscover
================================

A simple way to auto discover AJAX_LOOKUP_CHANNELS in settings.py by looking in lookups.py for registered apps.

Install this app with PIP using a GIT clone since this helper is not available in PyPi:

```console
pip install -e git+https://github.com/peterfarrell/django-ajax-selects-autodiscover.git#egg=django-ajax-selects-autodiscover --upgrade
```

In your `settings.py` file, replace your `AJAX_LOOKUP_CHANNELS` with:

```python
from ajax_selects_autodiscover import AutoDiscover

AJAX_LOOKUP_CHANNELS = AutoDiscover()
```

The `lookup.py` files is now where you define all your channels.  Here is an example:

```python
from ajax_select import LookupChannel

from login.models import Application


class ApplicationLookup(LookupChannel):
    model = Application

    def get_query(self, q, request):
        return Application.objects.find_active_by_name(q)


AJAX_LOOKUP_CHANNELS = {
    'application': ('shared.lookup', 'ApplicationLookup'),
}
```
