from django.conf import settings
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from guide.models import Supermarket

def index(request):
	markets = Supermarket.objects.all()
	t = loader.get_template('market/index.html')
	c = Context ({'object_list' : markets, 'STATIC_URL': settings.STATIC_URL})
	return HttpResponse(t.render(c))


@login_required
def market(request):
	markets = Supermarket.objects.all()
	t = loader.get_template('market/overview.html')
	c = Context ({'object_list' : markets, 'STATIC_URL': settings.STATIC_URL})
	return HttpResponse(t.render(c))


def contact(request):
	return render_to_response('site/contact.html', {'STATIC_URL': settings.STATIC_URL})
	
def imprint(request):
	return render_to_response('site/imprint.html', {'STATIC_URL': settings.STATIC_URL})