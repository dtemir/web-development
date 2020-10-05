from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import CommentForm, CommentFormNotAuth, PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class PostList(ListView):

    template_name = 'blog/blog.html'

    def __init__(self):
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        context_object_name = 'post_list'
        paginate_by = 3
        self.queryset = queryset
        self.context_object_name = context_object_name
        self.paginate_by = paginate_by
        super().__init__()


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # If someone posts a comment
    # Check if user is authenticated
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Initialize a comment object, but don't commit yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Activate the comment, since the user is logged in
            new_comment.active = True
            # Save it
            new_comment.save()

    elif request.method == 'POST' and not request.user.is_authenticated:
        comment_form = CommentFormNotAuth(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        if request.user.is_authenticated:
            comment_form = CommentForm()
        else:
            comment_form = CommentFormNotAuth()

    likes = get_object_or_404(Post, slug=slug)
    total_likes = likes.total_likes()

    liked = False
    if likes.likes.filter(id=request.user.id):
        liked = True

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'total_likes': total_likes,
                                           'liked': liked,
                                           })


def CategoryView(request, category):
    template_name = 'blog/categories.html'
    category_posts = Post.objects.filter(category=category.replace('-', ' ')).order_by('-created_on')

    return render(request, template_name, {'category_posts': category_posts,
                                           'cat': category.title(),
                                           })


def LikeView(request, slug):
    post = get_object_or_404(Post, slug=request.POST.get('post_slug'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blog:post_detail', args=[slug]))


class AddPostView(CreateView):

    def __init__(self):
        self.model = Post
        self.form_class = PostForm
        super().__init__()

    template_name = 'blog/add_post.html'


class EditPostView(UpdateView):

    def __init__(self):
        self.model = Post
        self.form_class = EditForm
        super().__init__()

    template_name = 'blog/edit_post.html'


class DeletePostView(DeleteView):

    def __init__(self):
        self.model = Post
        self.success_url = reverse_lazy('blog:home')
        super().__init__()

    template_name = 'blog/delete_post.html'


class AddCategoryView(CreateView):

    def __init__(self):
        self.model = Category
        self.fields = '__all__'
        super().__init__()

    template_name = 'blog/add_category.html'
