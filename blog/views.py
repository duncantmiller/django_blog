from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.order_by("published_at")
    return render(request, 'index.html', {"articles": articles})

def article(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, "article.html", {
        "article": article,
        "author": article.author,
        "tags": article.tags.all()
    })
