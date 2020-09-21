from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import CommentForm, PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


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

    likes = get_object_or_404(Post, slug=slug)
    total_likes = likes.total_likes()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'total_likes': total_likes,
                                           })


def CategoryView(request, category):
    template_name = 'blog/categories.html'
    category_posts = Post.objects.filter(category=category).order_by('-created_on')

    return render(request, template_name, {'category_posts': category_posts})


def LikeView(request, slug):
    post = get_object_or_404(Post, slug=request.POST.get('post_slug'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog:post_detail', args=slug))


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = PostForm


class EditPostView(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    form_class = EditForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    fields = '__all__'