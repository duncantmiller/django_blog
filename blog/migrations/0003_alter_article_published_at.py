# Generated by Django 5.0 on 2023-12-13 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
    ]