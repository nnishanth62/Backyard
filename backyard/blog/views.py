from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

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
    form_class = PostForm #from forms.py
    #fields = "__all__"
    #fields = ("title", "body")

class UpdatePostView(UpdateView): 
    model = Post 
    form_class = EditForm
    template_name = "update_post.html"
    #fields = ['title', 'title_tag','body'] #cant have this line and the form_class line

