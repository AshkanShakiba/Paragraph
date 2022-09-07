from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test-user",
            email="test@email.com",
            password="drowssap",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title="test-title",
            context="test-context",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "test-user")
        self.assertEqual(self.post.title, "test-title")
        self.assertEqual(self.post.context, "test-context")
        self.assertEqual(str(self.post), "test-title")
