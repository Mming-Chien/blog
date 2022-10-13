from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
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
			new_blog = form.save(commit = False)
			new_blog.owner = request.user
			new_blog.save()
			return redirect("blogs:index")
	# Display a blank or invalid form
	context = {"form": form}
	return render(request, "blogs/new_blog.html",context)

@login_required
def edit_blog(request,blog_id):
	""" Edit existing blog"""
	blog = get_object_or_404(BlogPost ,id=blog_id)
	# Make sure users edit their own posts
	if blog.owner != request.user:
		raise Http404


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