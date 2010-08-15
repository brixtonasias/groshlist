from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class RegisterForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))
	password_repeat = forms.CharField(widget=forms.PasswordInput(render_value=False))


class SupermarketForm(forms.Form):
	name = forms.CharField(max_length=255)
	street = forms.CharField(max_length=255)
	zipcode = forms.CharField(max_length=10)
	city = forms.CharField(max_length=255)
	description = forms.CharField(widget=forms.Textarea)


class ShoppingListForm(forms.Form):
	name = forms.CharField(max_length=255)
	description = forms.CharField(widget=forms.Textarea)
	date_created = forms.DateTimeField()
	date_updated = forms.DateTimeField()
