
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from blog.models import *

class CommentTestCase(LiveServerTestCase):

    def setUp(self):
        comment_1 = Comment.objects.create(body="Foo")
        author_1 = Author.objects.create(name="Bash Bar")
        self.article = Article.objects.create(
            title="title",
            subtitle="subtitle",
            body="body",
            author=author_1
        )
        self.article.comments.add(comment_1)

        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_can_make_a_comment(self):
        """a user can type in a comment and click submit and the comment will appear on the page"""
        article_url = self.live_server_url + f"/articles/{self.article.id}"
        self.driver.get(article_url)

        comment_input = self.driver.find_element("name", "comment_body")
        comment_input.send_keys("This is a test comment")

        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        self.assertIn("This is a test comment", self.driver.page_source)

if __name__ == "__main__":
    unittest.main()
