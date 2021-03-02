from django.shortcuts import render
from .models import Post #We import Post model from models. Using dot before models uses models from current directory. 
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #QuerySet
    return render(request, 'blog/post_list.html', {'posts': posts})

# Create your views here.
