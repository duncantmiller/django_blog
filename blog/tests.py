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

    def test_comments_count(self):
        self.assertEqual(self.article.comments_count(), 1)

    def test_has_comments(self):
        self.assertTrue(self.article.has_comments())

    def test_has_valid_article_page(self):
        c = Client()
        response = c.get(f"/articles/{self.article.id}/")
        self.assertEqual(response.status_code, 200)

class AuthorTestCase(TestCase):

    def setUp(self):
        self.author_1 = Author.objects.create(name="Bash Bar")
        Article.objects.create(title="title",
                               subtitle="subtitle",
                               body="body",
                               author=self.author_1
                               )

    def test_articles_count(self):
        self.assertEqual(self.author_1.articles_count(), 1)

class TagTestCase(TestCase):

    def setUp(self):
        self.tag_1 = Tag.objects.create(title="Foo")
        author_1 = Author.objects.create(name="Bash Bar")
        article = Article.objects.create(title="title",
                                         subtitle="subtitle",
                                         body="body",
                                         author=author_1)
        article.tags.add(self.tag_1)

    def test_articles_count(self):
        self.assertEqual(self.tag_1.articles_count(), 1)
