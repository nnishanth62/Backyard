from django.test import TestCase
from .models import Post

class BasicTest(TestCase):

    def setUp(self):
        self.post = Post()
        self.post.title = "This is a new test title"
        self.post.body = "test body"
        self.likes = total_likes()
        self.get_absolute_url()

    def test_fields(self):
        post = Post()
        post.title = "This is another test title"
        post.body = "another test body"
        total_likes()
        get_absolute_url()

        record = Post.objects.get(pk=post.pk)
        self.assertequal(record,post)

    def test_get_absolute_url(self):
        self.assertEqual(
            self.post.get_absolute_url(),
            "/%s/" % (self.post.pk)
        )

    def test_mark_completed(self):
        self.assertEqual(self.item.completed, False)
        self.item.mark_completed()
        self.assertEqual(self.item.completed, True)