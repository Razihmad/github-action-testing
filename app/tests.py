from django.test import TestCase
from .models import Blog


class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Blog.objects.create(title='My Blog Title', author='My Name', slug='my-blog-title')

    def test_blog_content(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = f'{blog.title}'
        self.assertEquals(expected_object_name, 'My Blog Title')
