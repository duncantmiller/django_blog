from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def show(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, "show.html", {"article": article})
