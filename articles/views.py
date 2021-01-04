from django.shortcuts import render
from .models import Articles
#  Create your views here.
#  FBV function based view  基于函数的视图
def index(request):
    articles=Articles.objects.all()
    context = {
        "articles":articles
    }
    return render(request,"index.html",context)


def detail(request,pk):
    article=Articles.objects.get(pk=pk)
    context = {
        "article":article
    }
    return render(request,"single_article.html",context)


def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")
