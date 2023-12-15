from django.test import TestCase
from blog.models import Author, Article, Tag

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
