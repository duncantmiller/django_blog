from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

class Article(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    published_at = models.DateTimeField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="articles")

    def __str__(self) -> str:
        return f"{self.id}: {self.title}"
