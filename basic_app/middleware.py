from audioop import reverse

from django.http import HttpResponseRedirect


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    def process_request(self, request,exception):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('index'))
        return None