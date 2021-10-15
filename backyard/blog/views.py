from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

'''
def home(request):
    return render(request, 'home.html', {})
'''


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    # ordering = ['-id']  # temporary, most recent post appears first


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'category.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class MakePostView(CreateView):
    model = Post
    template_name = "make_post.html"
    form_class = PostForm  # from forms.py
    # fields = "__all__"
    # fields = ("title", "body")


class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = "__all__"
    # fields = ("title", "body")


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    # fields = ['title', 'title_tag','body'] #cant have this line and the form_class line


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')
