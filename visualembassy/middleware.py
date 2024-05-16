from django.http import HttpResponseRedirect

class SubdomainRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]  # Remove port number
        path = request.path
        if 'rick.visualembassy.org' in host and path != '/founder/portfolio':
            return HttpResponseRedirect('/founder/portfolio')
        response = self.get_response(request)
        return response
