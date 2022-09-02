from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Post, Comment
from .forms import blogPostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse


# Create your views here.
def LikeView(request, pk):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user.id)
        liked=False
    else:
        post.likes.add(request.user.id)
        liked=True

    return HttpResponseRedirect(reverse('blogdetails',args=[str(post.author.username),str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'homecrud.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blogdetails.html'
    success_url = reverse_lazy('updatepost')

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"]= total_likes
        context["liked"] = liked
        return context


class AddBlogView(CreateView):
    model = Post
    form_class = blogPostForm
    template_name = 'addpost.html'


class UpdateBlogView(UpdateView):
    model = Post
    template_name = 'updatepost.html'
    form_class = EditForm

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'addcomment.html'
    #fields = '_all_'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
        
    success_url = reverse_lazy('homecrud')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('homecrud')