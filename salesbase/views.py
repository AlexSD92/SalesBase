# code for 404 and 500 handlers from:
# https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page

from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response