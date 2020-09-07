from django.test import TestCase, Client
from django.urls import reverse
from .models import Post
from .test_models import create_post
from . import views
import json


class TestAddPostView(TestCase):

    def test_add_post_form_visible(self):
        """
        Test that the form for adding posts is available
        """
        client = Client()

        response = client.get(reverse('blog:add_post'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_post.html')


class TestEditPostView(TestCase):

    def test_edit_post_form_visible(self):
        """
        Test that the form for editing posts is available
        """
        client = Client()
        post = create_post(title="Title", slug="title", content="Lots of text goes in here", status=1)

        url = reverse('blog:edit_post', args=(post.slug,))
        print(url)
        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_post.html')