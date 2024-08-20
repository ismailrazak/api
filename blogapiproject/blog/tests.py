from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
# Create your tests here.
class Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user=get_user_model()
        cls.user=cls.user.objects.create(name='ismail')
        cls.post=Post.objects.create(author=cls.user,title='sunny day',body='hello world')


    def test_post(self):
        self.assertEqual(Post.objects.count(),1)
        self.assertEqual(self.post.title,'sunny day')
        self.assertEqual(self.post.author,self.user)
        self.assertEqual(str(self.post),'sunny day')
