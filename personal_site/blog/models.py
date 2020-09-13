from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.CharField(max_length=255, default='coding')


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title[:50]

    # used for sitemap to specify the url location (also used by AddPostView)
    def get_absolute_url(self):

        return reverse('blog:post_detail', kwargs={'slug': str(self.slug)})


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('blog:home')


class Comment(models.Model):
    # related_name is used to avoid calling post.comment_set.all() when fetching all
    # comments for a post. Instead, I'll use post.comments.all()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body[:10], self.name)
