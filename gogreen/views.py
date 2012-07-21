from django.shortcuts import render_to_response, get_object_or_404
from gogreen.models import *
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import RequestContext
from django.core import serializers
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from decimal import *
import logging
from django.utils import simplejson
from mezzanine.utils.views import paginate


def home(request):

#        thebattle = get_object_or_404(Battle, is_homepage=True)
#        initial_poll_results = get_poll_results(thebattle)
#        #ORDER BY PUBDATE (MOST RECENT)
##        featured_videos = Battle.objects.filter(status=2).filter(is_featured=True)[:8]
#        featured_videos = Battle.objects.filter(status=2).filter(is_featured=True)
##        logger.debug('View: home - Success')
    return render_to_response('index.html',
                            {},
                             context_instance=RequestContext(request))
