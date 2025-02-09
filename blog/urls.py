from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path(
        "post/<int:id>/<slug:slug>/",
        views.article_detail_view,
        name="post-detail",
    ),
    path("create-post/", views.create_post_view, name="create-post"),
    # path for the delete user's own comment
    path(
        "delete-comment/<int:comment_id>/", views.delete_comment, name="delete-comment"
    ),
]
