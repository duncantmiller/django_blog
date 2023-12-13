from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    published_at = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.id}: {self.title}"
