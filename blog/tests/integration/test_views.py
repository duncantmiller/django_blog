from django.test import Client, TestCase
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

    def test_has_valid_article_page(self):
        c = Client()
        response = c.get(f"/articles/{self.article.id}/")
        self.assertEqual(response.status_code, 200)
