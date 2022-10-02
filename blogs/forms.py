from django import forms 
from .models import BlogPost

class BlogForm(forms.ModelForm):
	"""Form for adding new blogs"""
	class Meta:
		model = BlogPost
		fields = ['title','text']
		labels = {'title':'', 'text':'',}
		widget = {'text': forms.Textarea(attrs={'cols' : 100})}