from django.test import TestCase

from .models import *

class ArticleTestCase(TestCase):

    def setUp(self):

         tag_1 = Tag.objects.create(title="Foo")

         author_1 = Author.objects.create(name="Bash Bar")

         article = Article.objects.create(title="title",
                                          subtitle="subtitle",
                                          body="body",
                                          author=author_1
                                          )
         article.tags.add(tag_1)

    def test_articles_count(self):
         author = Author.objects.get(name="Bash Bar")
         self.assertEqual(author.articles_count(), 1)
