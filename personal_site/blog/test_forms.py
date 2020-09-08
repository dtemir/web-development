from django.test import TestCase, Client
from .forms import PostForm, EditForm
from .test_models import create_post
from django.shortcuts import reverse

post = create_post(title="Title Test Form", slug="title-test-form", content="Lots of text goes in here",
                   status=1)


class PostFormTest(TestCase):

    def test_post_form_POST(self):

        data = {'title': 'Title Test PostForm',
                'slug': 'title-test-postform',
                'author': post.author,
                'content': 'Lots of text goes in here',
                'status': 1, }
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

        case = form.save()
        self.assertEqual(case.title, 'Title Test PostForm')


class EditFormTest(TestCase):

    def test_edit_form_POST(self):

        client = Client()

        data = {'title': 'Title Test EditForm',
                'slug': 'title-test-editform',
                'author': post.author,
                'content': 'This text has been updated',
                'status': 1, }

        form = EditForm(instance=post, data=data)

        self.assertTrue(form.is_valid())

        case = form.save()
        self.assertEqual(case.title, data['title'])

        # response = self.client.post(
        #     reverse('blog:edit_post', args=(post.slug,))
        # )
        #
        # self.assertEqual(response.status_code, 302)
        #
        # self.assertEqual(post.title, 'Test Title')
