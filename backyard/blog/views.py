from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

'''
def home(request):
    return render(request, 'home.html', {})
'''
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class MakePostView(CreateView):
    model = Post
    template_name = "make_post.html"
    fields = "__all__"
    #fields = ("title", "body")
