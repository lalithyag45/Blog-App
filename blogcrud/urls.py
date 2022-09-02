from django.urls import path
from . import views
from .views import  HomeView,AddBlogView,UpdateBlogView,DeletePostView,ArticleDetailView,LikeView, AddCommentView
urlpatterns = [
    path('',HomeView.as_view(),name='homecrud'),
    path('user/<str:usern>/<int:pk>',ArticleDetailView.as_view(),name='blogdetails'),
    path('addpost/',AddBlogView.as_view(),name='addpost'),
    path('blog/updatepost/<int:pk>',UpdateBlogView.as_view(),name='updatepost'),
    path('blog/<int:pk>/deletepost',DeletePostView.as_view(),name='deletepost'),
    path('like/<int:pk>',views.LikeView,name='like_post'),
    path('blog/<int:pk>/comment/',AddCommentView.as_view(),name='addcomment'),
]
