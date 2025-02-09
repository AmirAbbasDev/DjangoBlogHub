from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm, CommentForm
from .models import Comment, Post
import re


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
    return render(request, "blog/create_post.html", context)


def new_func(form, post):
    """
    Creates the slug for a new blog post.

    This function takes a form instance and a post instance as arguments and creates the slug
    for the post by removing all special characters, replacing spaces with hyphens, and converting the string to lowercase.
    """
    slug = re.sub(r"[^\w\s-]", "", form.cleaned_data["title"])
    slug = re.sub(r"\s+", "-", slug)  # Replace spaces with hyphens
    post.slug = slug.lower()


def article_detail_view(request, id, slug):
    """
    Displays a blog post with its comments and allows authenticated users to leave new comments.

    This view takes the post ID and slug as arguments and renders the post detail template with the post data,
    a form for submitting a new comment, and a list of existing comments ordered by newest first.

    If the request is a POST, the view validates the form and saves the new comment. If the user is not
    authenticated, the view redirects to the login page.
    """
    # Fetch the post or return a 404 if it doesn't exist
    post = get_object_or_404(Post, id=id, slug=slug)

    # Initialize the comment form and fetch existing comments
    form = CommentForm()
    comments = Comment.objects.filter(post=post).order_by(
        "-created_at"
    )  # Order comments by newest first

    # Handle POST requests (comment submission)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")  # Redirect to login if user is not authenticated

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(
                "post-detail", id=id, slug=slug
            )  # Redirect to the same post after commenting

    # Prepare context for rendering the template
    context = {
        "form": form,
        "comments": comments,
        "post": post,
    }

    return render(request, "blog/post_detail.html", context)


# delete user's own comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure the logged-in user owns the comment
    if request.user == comment.user or request.user.is_staff:
        comment.delete()
        return redirect("post-detail", id=comment.post.id, slug=comment.post.slug)
    else:
        return redirect(
            "post-detail", id=comment.post.id, slug=comment.post.slug
        )  # Redirect if not allowed to delete
