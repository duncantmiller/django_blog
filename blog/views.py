from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Article, Comment

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
        "tags": article.tags.all(),
        "comments": article.comments.all()
    })

def comment(request, article_id):
    if request.method == "POST":
        article = Article.objects.get(pk=article_id)
        comment_body = request.POST["comment_body"]
        comment = Comment(body=comment_body)
        comment.save()
        article.comments.add(comment)
        return HttpResponseRedirect(reverse("article", args=(article.id,)))
