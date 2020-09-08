from django.test import TestCase, Client
from django.urls import reverse
from .test_models import create_post
from . import views


class TestAddPostView(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('blog:add_post')

    def test_add_post_form_GET(self):
        """
        Test that the view with the form for adding posts is available
        """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_post.html')


class TestEditPostView(TestCase):

    def setUp(self):
        self.client = Client()
        post = create_post(title="Title Test EditPostView", slug="title-test-editpostview",
                           content="Lots of text goes in here", status=1)
        self.url = reverse('blog:edit_post', args=(post.slug,))

    def test_edit_post_form_GET(self):
        """
        Test that the view with the form for editing posts is available
        """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_post.html')

