from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, get_object_or_404

from django.core.context_processors import csrf

from guide.models import Supermarket
from guide.forms import SupermarketForm
from guide.forms import LoginForm
from guide.forms import RegisterForm


def index(request):
	return render_to_response('site/homepage.html', 
		context_instance=RequestContext(request)
	)


def jquery_test(request):
	if request.is_ajax():
		print "Ajax call"
	else:
		print "No Ajax call"
	return render_to_response('jstest/jstest.html', context_instance=RequestContext(request))


def jquery_data_test(request):
	message = "No Ajax."
        if request.is_ajax():
		if request.method == 'GET':
			message = "This is an XHR GET request"
		elif request.method == 'POST':
			message = "This is an XHR POST request"
			# Here we can access the POST data
			print request.POST
		else:
			message = "No XHR"
	return HttpResponse(message)


@login_required(redirect_field_name='next')
def createmarket(request, id):
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
			return HttpResponseRedirect('/market')
	else:
		form = SupermarketForm()
		return render_to_response('market/detail.')


@login_required(redirect_field_name='next')
def market_edit(request, market_id):
	
	market = Supermarket.objects.get(id=market_id)
	
	if request.method == 'POST':
		form = SupermarketForm(request.POST, market)
		rc = RequestContext(request)
		if form.is_valid():
			market.name = form.cleaned_data['name']
			market.street = form.cleaned_data['street']
			market.zipcode = form.cleaned_data['zipcode']
			market.city = form.cleaned_data['city']
			market.description = form.cleaned_data['description']
			market.update()
			return HttpResponseRedirect('/market/detail.html?market_id=%s' % market.id)
	else:
		form = SupermarketForm(market)
		return render_to_response('market/edit.html', {
			'market': market,
		}, context_instance=RequestContext(request))


@login_required(redirect_field_name='next')
def market_detail(request, market_id):
	market = Supermarket.objects.get(id=market_id)
	return render_to_response('market/detail.html', {		
		'market': market,
	}, context_instance=RequestContext(request))


@login_required(redirect_field_name='next')
def market(request):
	markets = Supermarket.objects.all()
	return render_to_response('market/overview.html', {
		'object_list': markets,
	}, context_instance=RequestContext(request))


def register(request):
	
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
					return render_to_response('registration/login.html', {
						'form': LoginForm(),
					}, context_instance=RequestContext(request))
	else:
		form = RegisterForm()
		
	return render_to_response('registration/register.html', {
		'form': form,
	}, context_instance=RequestContext(request))


def contact(request):
	return render_to_response('site/contact.html', 
		context_instance=RequestContext(request)
	)


def imprint(request):
	return render_to_response('site/imprint.html', 
		context_instance=RequestContext(request)
	)
