from django.conf.urls.defaults import patterns, url, include


urlpatterns = patterns('beefycachecontrol.tests.views',
    url(r'^test-no-decorator/$', 'test_no_decorator',
        name='beefy-test-no-decorator'),
    url(r'^test-never-cache/$', 'test_never_cache',
        name='beefy-test-never-cache'),
    url(r'^test-cache-control/$', 'test_cache_control',
        name='beefy-test-cache-control'),
    url(r'^test-set-header/$', 'test_set_header',
        name='beefy-test-set-header'),
)
