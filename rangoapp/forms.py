from django import forms
from django.contrib.auth.models import User
from rangoapp.models import Page, Category, UserProfile

class CategoryForm(forms.ModelForm):
  name = forms.CharField(max_length=128, help_text="Enter the category name:")
  likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
  views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
  slug = forms.CharField(widget=forms.HiddenInput(), required=False)

  class Meta:
    model = Category
    fields = ('name',)

class PageForm(forms.ModelForm):
  title = forms.CharField(max_length=128, help_text="Enter the title of the page:")
  url = forms.URLField(max_length=200, help_text="Enter the URL:")
  views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

  class Meta:
    model = Page
    exclude = ('category',)

  def clean(self):
    cleaned_data = self.cleaned_data
    url = self.cleaned_data.get('url')
    prefix = 'http://'

    if url and not url.startswith(prefix):
      url = prefix + url
      cleaned_data['url'] = url

    return cleaned_data

class UserForm(forms.ModelForm):
  username = forms.CharField(help_text="Enter the desired username:", max_length=50)
  email = forms.EmailField(help_text="Enter your email:")
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta:
    model = User
    fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
  website = forms.URLField(max_length=200, help_text="Add your website(optional):", required=False)
  picture = forms.ImageField(help_text="Upload a profile image:", required=False)

  class Meta:
    model = UserProfile
    fields = ('website', 'picture',)