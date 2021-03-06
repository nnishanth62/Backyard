from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# from .projectSD.Backyard.backyard.backyard import settings

'''
def home(request):
    return render(request, 'home.html', {})
'''


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():  # if a like already exists remove it
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)  # if a like doesn't exist add it
        liked = True

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
    # if user.is_authenticated:
    #   return HttpResponseRedirect(reverse('register'))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    # ordering = ['-id']  # temporary, most recent post appears first

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'category.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class MakePostView(CreateView):
    model = Post
    template_name = "make_post.html"
    form_class = PostForm  # from forms.py
    # fields = "__all__"
    # fields = ("title", "body")


class AddCommentView(CreateView):
    model = Comment
    template_name = "add_comment.html"
    form_class = CommentForm  # from forms.py

    def form_valid(self,
                   form):  # make user id available to profile so that when the form is saved, it's under the right user
        form.instance.post_id = self.kwargs['pk']  # User is filling out form, grab user, to make it available to form
        return super().form_valid(form)

    success_url = reverse_lazy('home')


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
