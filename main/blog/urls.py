from django.urls import path
# from . import views
from .views import HomeView, PostDetailView, MakePostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name = "home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('make_post/', MakePostView.as_view(), name="make_post"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('post/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),


]
