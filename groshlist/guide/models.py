import datetime

from django.db import models
from django.contrib.auth.models import User


class Supermarket(models.Model):
	"""
	A Supermarket selling goods
	
	Test:
	
	>>> sm = Supermarket()
	>>> sm.name = 'Lidl'
	>>> sm.city = 'Muehlacker'
	>>> sm.user = User.objects.create(username='testusersm', password='testpw')
	>>> print sm
	Lidl, Muehlacker
	>>> print sm.user.username
	testusersm
	"""
	name = models.CharField(max_length=255)
	street = models.CharField(max_length=255)
	zipcode = models.CharField(max_length=10)
	city = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	user = models.ForeignKey(User, related_name="supermarkets")
	
	def __unicode__(self):
		return '%s, %s' % (self.name, self.city)


class Category(models.Model):
	"""
	Stuff you are able to buy belongs to a category
	
	Test:
	
	>>> c = Category()
	>>> c.name = 'Fresh Meat'
	>>> c.slug = 'fresh_meat'
	>>> c.order = 1
	>>> c.description = 'Where the fresh meat can be found'
	>>> c.supermarket = Supermarket.objects.create(name='Lidl', city='Muehlacker', user=User.objects.create(username='testusercat', password='testpw'))
	>>> print c
	Fresh Meat
	>>> print c.supermarket
	Lidl, Muehlacker
	"""
	name = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	description = models.TextField(blank=True)
	supermarket = models.ForeignKey(Supermarket, related_name='categories')
	order = models.IntegerField(blank=False, null=False, unique=True)
	
	def __unicode__(self):
		return '%s' % self.name


class Unit(models.Model):
	"""
	Could be kg, t, mg, l, ml
	
	Test:
	
	>>> u = Unit()
	>>> u.name = 'kg'
	>>> u.description = '1 kg = 1000 gramms'
	>>> print u
	kg
	"""
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name



class Currency(models.Model):
	"""
	The currency a ShoppingItem is valued in
	Could be Euro, Dollar, etc.
	
	Test:
	
	>>> cu = Currency()
	>>> cu.name = 'Euro'
	>>> cu.description = 'Payable in Europe'
	>>> cu.slug = 'Eur'
	>>> print cu
	Euro
	>>> print cu.slug
	Eur
	"""
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	slug = models.SlugField(unique=True)
	
	def __unicode__(self):
		return self.name


class ShoppingList(models.Model):
	"""
	A list belongs to a user and contains several ShoppingItems
	
	Test:
	
	>>> shlist = ShoppingList()
	>>> shlist.name = 'Shopping for Thanks Giving'
	>>> shlist.description = '10 people are coming'
	>>> shlist.user = User.objects.create(username='testusershlist', password='testpw')
	>>> print shlist
	Shopping for Thanks Giving
	>>> print shlist.description
	10 people are coming
	"""
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	date_created = models.DateTimeField(auto_now_add=True, editable=False)
	date_updated = models.DateTimeField(auto_now=True, editable=False)
	user = models.ForeignKey(User, related_name='shopping_lists')
	
	def __unicode__(self):
		return self.name


class ShoppingItem(models.Model):
	"""
	One item addable to a shopping list
	
	Test:
	
	>>> shlist = ShoppingList.objects.create(name='breakfast stuff', user=User.objects.create(username='testusershi', password='testpw'))
	>>> si = ShoppingItem()
	>>> si.shlist = shlist
	>>> si.name = 'Milk'
	>>> si.amount = '2'
	>>> si.unit = Unit.objects.create(name='l')
	>>> si.price = 0.25
	>>> si.currency = Currency.objects.create(name='Euro', slug='Eur')
	>>> print si
	Milk
	>>> print si.price
	0.25
	>>> print si.unit
	l
	>>> print si.currency.slug
	Eur
	"""
	name = models.CharField(max_length=255)
	amount = models.IntegerField(blank=False, null=False)
	unit = models.ForeignKey(Unit, related_name='Unit')
	price = models.IntegerField(blank=True)
	currency = models.ForeignKey(Currency)
	shlist = models.ForeignKey(ShoppingList, related_name='items')
	
	def __unicode__(self):
		return self.name