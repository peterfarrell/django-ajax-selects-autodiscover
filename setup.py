from setuptools import setup


setup(
    name="django-ajax-selects-autodiscover",
    version='alpha',
    author="Peter J. Farrell",
    author_email="pfarrell@greatbiztools.com",
    description="A simple way to auto discover AJAX_LOOKUP_CHANNELS in settings.py by looking in lookups.py for registered apps.",
    license="MIT",
    url="https://github.com/peterfarrell/django-ajax-selects-autodiscover",
    packages=[
        'ajax_selects_autodiscover',
    ],
    include_package_data=True,
    zip_safe=False,
)