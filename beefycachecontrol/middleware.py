from django.utils.cache import patch_cache_control


class BeefyCacheControlMiddleware(object):
    """
    Beefs up the Cache-Control HTTP header. Appends 'no-cache, no-store' when
    response should not be cached.
    """
    def process_response(self, request, response):
        if (response.has_header('Cache-Control') and
            'max-age=0' in str(response['Cache-Control'])):
            if 'no-cache' not in str(response['Cache-Control']):
                patch_cache_control(response, no_cache=True)
            if 'no-store' not in str(response['Cache-Control']):
                patch_cache_control(response, no_store=True)
        return response
