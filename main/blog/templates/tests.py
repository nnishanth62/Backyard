from django.test import TestCase
from .models import Post

class BasicTest(TestCase):
    def test_fields(self):
        post = Post()
        post.title = "This is a test title"
        post.body = "test body"
        total_likes()
        get_absolute_url()

        record = Post.objects.get(pk=1)
        self.assertequal(record,post)
