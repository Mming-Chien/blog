"""Define url patterns for blogs"""
from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
	#Home page
	path("", views.index , name = "index"),
	# Page for adding new blogs
	path("new_blog", views.new_blog, name="new_blog"),
	# Page for editing blog
	path("edit_blog/<int:blog_id>/", views.edit_blog, name= "edit_blog"),

]