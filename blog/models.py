from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"

    def articles_count(self):
        return self.articles.count()

class Tag(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f"{self.id}: {self.title}"

    def articles_count(self):
        return self.articles.count()

class Comment(models.Model):
    body = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    published_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="articles")
    tags = models.ManyToManyField(Tag, blank=True, related_name="articles")
    comments = models.ManyToManyField(Comment, blank=True, related_name="comments")

    def __str__(self) -> str:
        return f"{self.id}: {self.title}"

    def comments_count(self):
        return self.comments.count()

    def has_comments(self):
        return self.comments_count() > 0
