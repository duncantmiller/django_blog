from django.test import TestCase
from blog.models import *

class ArticleTestCase(TestCase):

    def setUp(self):
        comment_1 = Comment.objects.create(body="Foo")
        author_1 = Author.objects.create(name="Bash Bar")
        self.article = Article.objects.create(title="title",
                                              subtitle="subtitle",
                                              body="body",
                                              author=author_1
                                              )
        self.article.comments.add(comment_1)

    def test_comments_count(self):
        self.assertEqual(self.article.comments_count(), 1)

    def test_has_comments(self):
        self.assertTrue(self.article.has_comments())
