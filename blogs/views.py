from django.shortcuts import render
from .models import BlogPost
# Create your views here.

def index(request):
	""" The home page for blogs """
	blogs = BlogPost.objects.order_by("date_added")
	context = {"blogs": blogs}
	return render(request, "blogs/index.html", context)