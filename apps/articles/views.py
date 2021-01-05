from django.shortcuts import render
from .models import Articles,Category,Tag
from django.core.paginator import Paginator
from django.db.models import Q
#  Create your views here.
#  FBV function based view  基于函数的视图
def index(request):
    articles=Articles.objects.all()

    limited = 2
    p = Paginator(articles,limited)
    try:
        page = request.GET.get("page",1)
    except PageNotFound:
        page = 1

    
    articles = p.get_page(page)
    #前五文章
    lastest_articles = Articles.objects.all()[:5]
    #所有分类
    categroies = Category.objects.all()
    #标签
    tags = Tag.objects.all()
    context = {
        "articles":articles,
        "lastest_articles":lastest_articles,
        "categroies":categroies,
        "tags":tags
    }
    return render(request,"index.html",context)


def detail(request,pk):
    article=Articles.objects.get(pk=pk)
    article.increace_visited()
    lastest_articles = Articles.objects.all()[:5]
    #所有分类
    categroies = Category.objects.all()
    #标签
    tags = Tag.objects.all()
    context = {
        "article":article,
        "lastest_articles":lastest_articles,
        "categroies":categroies,
        "tags":tags
    }
    return render(request,"single_article.html",locals())


def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")


def search(request):
    keyword = request.GET.get('keyword')
    print(keyword)
    if not keyword:
        err_msg = "请输入关键字"
        return render(request,'index.html',locals())
    articles = Articles.objects.filter(Q(title__icontains= keyword)|Q(abstract__icontains= keyword)|Q(content__icontains=keyword))
    limited = 2
    p = Paginator(articles,limited)
    try:
        page = request.GET.get('page',1)
    except PageNotFound:
        page = 1

    articles = p.get_page(page)
    lastest_articles = articles[:5]
    #所有分类
    categroies = Category.objects.all()
    #标签
    tags = Tag.objects.all()
    return render(request,"index.html",locals())