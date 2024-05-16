from django.http import HttpResponseRedirect
import logging
logger = logging.getLogger(__name__)

class SubdomainRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]  # Remove port number
        path = request.path
        logger.debug(f"Host: {host}, Path: {path}")
        if 'rick.visualembassy.org' in host and path != '/founder/portfolio/':
            logger.debug("Redirecting to /founder/portfolio/")
            return HttpResponseRedirect('/founder/portfolio/')
        response = self.get_response(request)
        return response
