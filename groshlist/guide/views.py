from django.conf import settings
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required

from guide.models import Supermarket

def index(request):
	markets = Supermarket.objects.all()
	t = loader.get_template('market/index.html')
	c = Context ({'object_list' : markets, 'STATIC_URL': settings.STATIC_URL})
	return HttpResponse(t.render(c))


def market(request):
	markets = Supermarket.objects.all()
	t = loader.get_template('market/overview.html')
	c = Context ({'object_list' : markets, 'STATIC_URL': settings.STATIC_URL})
	return HttpResponse(t.render(c))