from django.shortcuts import render
from .models import Post
from django.http import Http404
# from django.contrib.auth.decorators import login_required


# @login_required
def index(request):
    return render(request, "blog/index.html")


# Display the list of blog posts
# def post_list(request):
#     posts = Post.published.all()
#     return render(request, "blog/post/list.html", {"posts": posts})


# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404("No Post found.")
#     return render(request, "blog/post/detail.html", {"post": post})
