from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogForm
# Create your views here.

def index(request):
	""" The home page for blogs """
	blogs = BlogPost.objects.order_by("date_added")
	context = {"blogs": blogs}
	return render(request, "blogs/index.html", context)

@login_required
def new_blog(request):
	""" The page for adding new blog"""
	if request.method != 'POST':
		# No data added, create a blank form
		form = BlogForm()
	else:
		# POST data submitted, process data
		form = BlogForm(data =  request.POST)
		if form.is_valid():
			new_log = form.save()
			return redirect("blogs:index")
	# Display a blank or invalid form
	context = {"form": form}
	return render(request, "blogs/new_blog.html",context)

@login_required
def edit_blog(request,blog_id):
	""" Edit existing blog"""
	blog = BlogPost.objects.get(id=blog_id)
	if request.method != "POST":
		# Initial request, pre-fill form with the current blog
		form = BlogForm(instance=blog )
	else:
		# POST date submitted, process data
		form = BlogForm(instance=blog, data = request.POST)
		if form.is_valid():
			form.save()
			return redirect("blogs:index")
	context = {"blog": blog,"form": form}
	return render(request, "blogs/edit_blog.html", context)