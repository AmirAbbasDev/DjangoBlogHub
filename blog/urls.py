from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path(
        "post/<int:id>/<slug:slug>/",
        views.article_detail_view,
        name="post_detail",
    ),
    path("create-post/", views.create_post_view, name="create-post"),
]
