from django.shortcuts import render, redirect
from .models import Post
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm


# Display the blog homepage
class PostListView(ListView):
    """
    A view for displaying a list of blog posts.

    This view uses the `Post` model and renders the list of posts using the `blog/index.html` template.
    It paginates the list of posts, displaying 5 posts per page, and only includes published posts.

    Attributes:
        model (Post): The model that this view will be working with.
        template_name (str): The HTML template that this view will use to render the list of posts.
        context_object_name (str): The name of the variable that will be used to access the list of posts in the template.
        paginate_by (int): The number of posts to display per page.
        queryset (QuerySet): The queryset that this view will use to retrieve the list of posts.
    """

    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 9
    queryset = Post.published.all()


@login_required
def create_post_view(request):
    """
    Handles the creation of a new blog post.

    This view handles both the GET and POST requests for creating a new blog post.
    If the request is a GET, it renders the post creation form.
    If the request is a POST, it validates the form and saves the new post.
    """
    if request.method == "POST":
        # Create a form instance with the submitted data
        form = PostForm(request.POST)
        if form.is_valid():
            # Create a new post instance from the form data
            post = form.save(commit=False)
            # Create the slug for the post
            new_func(form, post)
            # Set the author of the post to the current user
            post.author = request.user
            # Save the post to the database
            post.save()
            # Redirect the user to the index page
            return redirect("index")
    else:
        # Create an empty form instance for the GET request
        form = PostForm()
    # Render the post creation form
    context = {"form": form}
    return render(request, "blog/post.html", context)


def new_func(form, post):
    """
    Creates the slug for a new blog post.

    This function takes a form instance and a post instance as arguments and creates the slug
    for the post by replacing spaces with hyphens and converting the string to lowercase.
    """
    post.slug = form.cleaned_data["title"].replace(" ", "-").lower()

class ArticleDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context