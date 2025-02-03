from django.urls import path
from . import views
# Defining the app namespace
# app_name = 'blog'

# Defining the URL patterns

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path(
        "post/<int:id>/<slug:slug>/",
        views.ArticleDetailView.as_view(),
        name="post_detail",
    ),
    path("create-post/", views.create_post_view, name="create-post"),
    # path("<int:id>/", views.post_detail, name="post_detail"),
]
