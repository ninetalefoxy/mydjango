from django.shortcuts import render
#importing model article to render them inside html file
from .models import Article
from django.http import HttpResponse
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/index_article.html',{'articles':articles}) #created dictionary to render article models


def article_detail(request,slug):
    return HttpResponse(slug)