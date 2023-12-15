from django.test import TestCase
from blog.models import *

class ArticleTestCase(TestCase):

    def setUp(self):
        comment_1 = Comment.objects.create(body="Foo")
        author_1 = Author.objects.create(name="Bash Bar")
        article = Article.objects.create(title="title",
                                         subtitle="subtitle",
                                         body="body",
                                         author=author_1
                                         )
        article.comments.add(comment_1)

    def test_comment_count(self):
        article = Article.objects.first
        self.assertEqual(article.comment_count, 1)

class AuthorTestCase(TestCase):

    def setUp(self):
        author_1 = Author.objects.create(name="Bash Bar")
        Article.objects.create(title="title",
                               subtitle="subtitle",
                               body="body",
                               author=author_1
                               )

    def test_articles_count(self):
        author = Author.objects.get(name="Bash Bar")
        self.assertEqual(author.articles_count(), 1)

class TagTestCase(TestCase):

    def setUp(self):
        tag_1 = Tag.objects.create(title="Foo")
        author_1 = Author.objects.create(name="Bash Bar")
        article = Article.objects.create(title="title",
                                         subtitle="subtitle",
                                         body="body",
                                         author=author_1)
        article.tags.add(tag_1)

    def test_articles_count(self):
        tag = Tag.objects.get(title="Foo")
        self.assertEqual(tag.articles_count(), 1)
