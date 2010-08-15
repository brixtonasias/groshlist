from django.conf import settings
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response

from django.core.context_processors import csrf

from guide.models import Supermarket
from guide.forms import LoginForm
from guide.forms import RegisterForm


def index(request):
	return render_to_response('site/homepage.html', {'STATIC_URL': settings.STATIC_URL}, RequestContext(request))


@login_required(redirect_field_name='/login')
def market(request):
	markets = Supermarket.objects.all()
	t = loader.get_template('market/overview.html')
	c = Context ({'object_list' : markets, 'STATIC_URL': settings.STATIC_URL})
	return HttpResponse(t.render(c))


def userlogout(request):
	logout(request)
	return render_to_response('site/contact.html')

def userlogin(request):	
	c = {}
	c.update(csrf(request))
	
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user_name = form.cleaned_data['username']
			user_pass = form.cleaned_data['password']
			user = authenticate(username=user_name, password=user_pass)
			if user is not None:
				if user.is_active:
					login(request, user)
					c.update({'user': user})
					rc = RequestContext(request, c)
					print user.is_authenticated()
					print user.email
					print "Correct username/password"
				else:
					print "Account disabled"
			else:
				print "Username + Password incorrect"
			return render_to_response('site/contact.html', {'STATIC_URL': settings.STATIC_URL}, rc)
	else:
		form = LoginForm()
		
	c.update({'STATIC_URL': settings.STATIC_URL, 'form': form,})
		
	return render_to_response('registration/login.html', c)


def register(request):
	c = {}
	c.update(csrf(request))
	
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			print 'Form is valid'
	else:
		form = RegisterForm()
		
	c.update({'STATIC_URL': settings.STATIC_URL, 'form': form,})
	
	return render_to_response('registration/register.html', {'form': form, 'STATIC_URL': settings.STATIC_URL})


def contact(request):
	return render_to_response('site/contact.html', {'STATIC_URL': settings.STATIC_URL})


def imprint(request):
	return render_to_response('site/imprint.html', {'STATIC_URL': settings.STATIC_URL})