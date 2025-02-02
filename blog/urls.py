from django.urls import path
from . import views

# Defining the app namespace
# app_name = "blog"

# Defining the URL patterns

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.post_list, name="post_list"),
    path("<int:id>/", views.post_detail, name="post_detail"),
]
