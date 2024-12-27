from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from .models import Thread, Post
from .forms import PostForm, ThreadForm

class ThreadView(ListView):
    model = Thread
    template_name = "forumapp/thread_list.html"
    context_object_name = "thread_list"

class ThreadDetailView(DetailView):

    model = Thread
    template_name = "forumapp/thread_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ThreadForm()

        return context

class PostCreateView(CreateView):
    model = Post
    template_name = "forumapp/post_creation.html"
    form_class = PostForm       

class PostUpdateView(CreateView):
    model = Post
    template_name = "forumapp/post_update.html"
    form_class = PostForm

    success_url = reverse_lazy("thread_list")

    def get_success_url(self):
        return reverse_lazy("thread-detail",  kwargs={"pk":self.get_object().pk})


class ThreadUpdateView(UpdateView):
    model = Thread
    template_name = "forumapp/thread_update.html"
    success_url = reverse_lazy("thread_list")
    form_class = ThreadForm