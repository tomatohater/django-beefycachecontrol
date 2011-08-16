from django.http import HttpResponse
from django.views.decorators.cache import cache_control, never_cache


def test_no_decorator(request):
    """A test view with no decorator.
    """
    return HttpResponse()


@never_cache
def test_never_cache(request):
    """A test view with @never_cache decorator.
    """
    return HttpResponse()


@cache_control(max_age=0)
def test_cache_control(request):
    """A test view with @cache_control decorator.
    """
    return HttpResponse()


def test_set_header(request):
    """A test view with max-age set manually.
    """
    response = HttpResponse()
    response['Cache-Control'] = 'max-age=0'
    return response
