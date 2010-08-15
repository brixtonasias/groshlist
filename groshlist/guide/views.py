from django.conf import settings
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response

from django.core.context_processors import csrf

from guide.models import Supermarket
from guide.forms import SupermarketForm
from guide.forms import LoginForm
from guide.forms import RegisterForm


def index(request):
	return render_to_response('site/homepage.html', {'STATIC_URL': settings.STATIC_URL}, RequestContext(request))


@login_required(redirect_field_name='/market')
def market(request):	
	if request.method == 'POST':
		form = SupermarketForm(request.POST)
		rc = RequestContext(request)
		user = rc['user']
		if form.is_valid():
			name = form.cleaned_data['name']
			street = form.cleaned_data['street']
			zipcode = form.cleaned_data['zipcode']
			city = form.cleaned_data['city']
			description = form.cleaned_data['description']
			market = Supermarket(name=name, street=street, zipcode=zipcode, city=city, description=description, user=user)
			market.save()
	else:
		form = SupermarketForm()
	
	markets = Supermarket.objects.all()
	rc = RequestContext(request)
	return render_to_response('market/overview.html', {'object_list': markets, 'STATIC_URL': settings.STATIC_URL, 'form': form}, rc)


def userlogout(request):
	logout(request)
	rc = RequestContext(request)
	return render_to_response('site/homepage.html', {'STATIC_URL': settings.STATIC_URL}, rc)

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
				else:
					print "Account disabled"
			else:
				print "Username + Password incorrect"
			rc = RequestContext(request, c)
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
			user_name = form.cleaned_data['username']
			user = None
			try:
				user = User.objects.get(username__exact=user_name)
			except:
				pass
			
			if user is None:
				user_pass = form.cleaned_data['password']
				user_pass_repeat = form.cleaned_data['password_repeat']
				
				if user_pass == user_pass_repeat:
					user = User.objects.create(username=user_name)
					user.set_password(user_pass)
					user.save()
					rc = RequestContext(request, c)
					return render_to_response('registration/login.html', {'STATIC_URL': settings.STATIC_URL}, rc)
	else:
		form = RegisterForm()
		
	c.update({'STATIC_URL': settings.STATIC_URL, 'form': form,})
	rc = RequestContext(request, c)
	return render_to_response('registration/register.html', {'form': form, 'STATIC_URL': settings.STATIC_URL}, rc)


def contact(request):
	return render_to_response('site/contact.html', {'STATIC_URL': settings.STATIC_URL})


def imprint(request):
	return render_to_response('site/imprint.html', {'STATIC_URL': settings.STATIC_URL})