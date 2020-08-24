from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Post


def create_post(title, slug, content, status):
    """Create a post with the given values"""
    return Post(title=title, slug=slug, content=content, status=status)


class PostModelTests(TestCase):

    def test_no_posts(self):
        """
        If no posts exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available yet")
        self.assertQuerysetEqual(response.context['post_list'], [])

    def test_posts_with_status_0(self):
        """
        If an only post has status of 0, it is not displayed
        Instead, an appropriate message is shown
        """
        post = create_post("Title", "slug", "Lots of text goes in here", 0)
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available yet")
        self.assertQuerysetEqual(response.context['post_list'], [])

    # def test_posts_with_status_1(self):
    #     """
    #     If an only post has status of 1, it is displayed
    #     """
    #     post = create_post("Title", "slug", "Lost of text goes in here", 1)
    #     response = self.client.get(reverse('blog:home'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertQuerysetEqual(response.context['post_list'], ['<Post: Title>'])

