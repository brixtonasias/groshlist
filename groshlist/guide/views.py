from django.conf import settings
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from django.core.context_processors import csrf

from guide.models import Supermarket
from guide.forms import LoginForm

def index(request):
	return render_to_response('site/homepage.html', {'STATIC_URL': settings.STATIC_URL})


@login_required(redirect_field_name='/login')
def market(request):
	markets = Supermarket.objects.all()
	t = loader.get_template('market/overview.html')
	c = Context ({'object_list' : markets, 'STATIC_URL': settings.STATIC_URL})
	return HttpResponse(t.render(c))


def login(request):
	c = {}
	c.update(csrf(request))
	
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			return render_to_response('site/contact.html', {'STATIC_URL': settings.STATIC_URL})
	else:
		form = LoginForm()
		
	c.update({'STATIC_URL': settings.STATIC_URL, 'form': form,})
		
	return render_to_response('registration/login.html', c)


def contact(request):
	return render_to_response('site/contact.html', {'STATIC_URL': settings.STATIC_URL})


def imprint(request):
	return render_to_response('site/imprint.html', {'STATIC_URL': settings.STATIC_URL})