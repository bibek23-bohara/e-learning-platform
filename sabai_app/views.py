from django.shortcuts import render
from django.views.generic import ListView

from sabai_app.models import Post


class HomeView(ListView):
    name = Post
    template_name="sabai_notes/home.html"
    context_object_name="posts"
    queryset=Post.objects.filter(status="active", published_at__isnull=False)