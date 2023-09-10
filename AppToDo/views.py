from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView

from AppToDo.models import todomodel


# Create your views here.


class Home(ListView):
    model = todomodel
    template_name = 'AppToDo/index.html'
    context_object_name = 'tweets'


class DeleteTweet(DeleteView):
    model = todomodel
    template_name = 'AppToDo/delete.html'
    success_url = '/'


class Message(DetailView):
    model = todomodel
    template_name = 'AppToDo/message.html'
    context_object_name = 'tweets'


class PostTweet(CreateView):
    model = todomodel
    template_name = 'AppToDo/post.html'
    fields = ['title', 'description', 'date']
    success_url = '/'
