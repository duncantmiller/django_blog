from django.test import TestCase
from blog.models import Author, Article

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
