from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import CommentForm, PostForm


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'

    paginate_by = 3


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # If someone posts a comment
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Initialize a comment object, but don't commit yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save it
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = PostForm

    #fields = ('__all__')