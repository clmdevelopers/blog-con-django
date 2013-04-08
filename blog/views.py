# Create your views here.
from blog.models import Post
from django.shortcuts import render_to_response

def tagpage(request, tag):
	post = Post.objects.filter(taggs__name=tag)
	return render_to_response("tagpage.html",{"posts":post,"tag":tag})