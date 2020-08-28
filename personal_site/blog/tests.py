from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Post


def create_post(title, slug, content, status):
    """Create a post with the given values"""
    user = User.objects.create_user(username='test', email='', password='who_cares_what_is_it')
    return Post.objects.create(title=title, author=user, slug=slug, content=content, status=status)


class PostModelTests(TestCase):

    def test_no_posts(self):
        """
        If no posts exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available yet")
        self.assertQuerysetEqual(response.context['post_list'], [])

    def test_post_with_status_0(self):
        """
        If an only post has status of 0, it is not displayed
        Instead, an appropriate message is shown
        """
        post = create_post(title="Title", slug="slug", content="Lots of text goes in here", status=0)
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available yet")
        self.assertQuerysetEqual(response.context['post_list'], [])

    def test_post_with_status_1(self):
        """
         If an only post has status of 1, it is displayed
         """
        post = create_post(title="Title", slug="slug", content="Lost of text goes in here", status=1)
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: Title>'])

    def test_post_created_on_date(self):
        """
        Ensure that the post accurately reflects the date of creation
        """
        # Since timezone.now() object is very accurate, I format the date time string into omitting microseconds
        # This way we can compare if the created_on attribute is equal to the actual time of creation
        post = create_post(title="Title", slug="slug", content="Lost of text goes in here", status=1)
        time_created = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(time_created, response.context['post_list'][0].created_on.strftime("%Y-%m-%d %H:%M:%S"))


class PostDetailModelTest(TestCase):

    def test_post_with_status_1(self):
        """
        Since detail view can only be accessed for a post with status 1,
        we need to check that information provided on the detail view page is
        accurate
        """
        post = create_post(title="Title", slug="slug", content="Lost of text goes in here", status=1)
        url = reverse('blog:post_detail', args=(post.slug,))
        response = self.client.get(url)
        self.assertContains(response, post.content)  # check content is correct
        self.assertContains(response, post.title)  # check title is correct
        self.assertContains(response, post.author)  # check author is correct
