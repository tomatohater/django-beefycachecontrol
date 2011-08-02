django-beefycachecontrol
========================

django-beefycachecontrol is a Django middleware that beefs up the Cache-Control HTTP headers as created by @never_cache decorator.

Normally, when a view is decorated with @never_cache::

    @never_cache
    def my_view(request):
        ...

The resulting HTTP headers (among other things) includes::

    Cache-Control	max-age=0

While this should be sufficient to prevent the response from being cached upstream, but there may be circumstances where this is not enough. Enter django-beefiercachecontrol!

With BeefyCacheControlMiddleware enabled, these HTTP headers become::

    Cache-Control	max-age=0, no-cache, no-store

Cache that and you'd be arrested by the internet cops!


Installation
************

1. ``easy_install django-beefycachecontrol`` or ``pip install django-beefycachecontrol``

2. Add ``beefycachecontrol`` to your ``INSTALLED_APPS``

3. In settings.py add ``'beefycachecontrol.middleware.BeefyCacheControlMiddleware'`` to ``MIDDLEWARE_CLASSES``


Usage
******
django-beefycachecontrol is a middleware. Once it is enabled, there is nothing more to do. It simply fixes up your no-cache related HTTP headers.


Credits
********
`Drew Engelson`_

.. _`Drew Engelson`: http://github.com/tomatohater
