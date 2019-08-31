from django.shortcuts import render
from blog.models import Post
# Create your views here.
def get_index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts': posts})

def new_post(request):
	pass