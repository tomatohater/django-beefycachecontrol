from django.test import TestCase
from django.core.urlresolvers import reverse


class BeefyTests(TestCase):
    urls = 'beefycachecontrol.tests.urls'


    def test_no_decorator(self):
        """Test a view with no decorator.
        """
        url = reverse('beefy-test-no-decorator')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual('Cache-Control' not in response, True)


    def test_never_cache(self):
        """Test a view with @never_cache decorator.
        """
        url = reverse('beefy-test-never-cache')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual('Cache-Control' in response, True)

        cache_control = response['Cache-Control'].split(', ')
        self.assertEqual('max-age=0' in cache_control, True)
        self.assertEqual('no-cache' in cache_control, True)
        self.assertEqual('no-store' in cache_control, True)


    def test_cache_control(self):
        """Test a view with @cache_control decorator.
        """
        url = reverse('beefy-test-cache-control')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual('Cache-Control' in response, True)

        cache_control = response['Cache-Control'].split(', ')
        self.assertEqual('max-age=0' in cache_control, True)
        self.assertEqual('no-cache' in cache_control, True)
        self.assertEqual('no-store' in cache_control, True)


    def test_set_header(self):
        """Test a view with max-age set manually.
        """
        url = reverse('beefy-test-set-header')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual('Cache-Control' in response, True)

        cache_control = response['Cache-Control'].split(', ')
        self.assertEqual('max-age=0' in cache_control, True)
        self.assertEqual('no-cache' in cache_control, True)
        self.assertEqual('no-store' in cache_control, True)
