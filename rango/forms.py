from django import forms
from django.contrib.auth.models import User
from rango.models import Category,Page,UserProfile

class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Choose a username.")
	email = forms.CharField(help_text="Enter your email address.")	
	password = forms.CharField(widget=forms.PasswordInput(),help_text="Enter your password.")
	class Meta:
		model = User
		fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
	website = forms.URLField(help_text="Please enter your website.",required=False)
	picture = forms.ImageField(help_text="Select a profile picture to upload.",required=False)
	class Meta:
		model = UserProfile
		fields = ('website','picture')

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128,help_text="Enter the category name")
	views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	class Meta:
		model = Category

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128,help_text="Enter the page title")
	url = forms.URLField(max_length=200,help_text="Enter the page URL")
	views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	
	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
		if url and not url.startswith('http://'):
			url = 'http://'+url
			cleaned_data['url'] = url
		return cleaned_data

	class Meta:
		model = Page
		fields = ('title','url','views')

