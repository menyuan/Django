# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Column , Article
from django.shortcuts import redirect
from django import forms
from blog.form import ArticleForm
# Create your views here.

class ArticleForm(forms.Form):
    title = forms.CharField()
    slug = forms.CharField()

def index(request):
    home_display_columns=Column.objects.filter(home_display=True)
    nav_display_columns=Column.objects.filter(nav_display=True)

    return render(request,'index.html',{
        'home_display_columns':home_display_columns,
        'nav_display_columns':nav_display_columns,
    })


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'blog/column.html', {'column': column})


def article_detail(request,pk, article_slug):
    article = Article.objects.get(pk=pk)
    if article_slug!=article.slug:
        return redirect(article,permanent=True)
    return render(request, 'blog/article.html', {'article': article})

def add_form(request):
    if request.method == 'POST':
        """
        第三种，使用ModelForm
        article = ArticleForm(request.POST or None, request.FILES)
        if article.is_valid():
            article.save()
         """
        """
        第一种方法，使用普通的form提交
        title=request.POST['title']
        slug=request.POST['slug']
        content=request.POST['content']
        Article.objects.create(
            title=title,
            slug=slug,
            content=content
        )"""
        """
        第二种方法，使用django.forms.Form提交
        article=ArticleForm(request.POST)
        if article.is_valid():
            Article.objects.create(
                title=article.cleaned_data['title'],
                slug=article.cleaned_data['slug']
            )
        """
        return HttpResponse('数据提交成功!')
    else:
        article=ArticleForm()
    return render(request,'blog/add_form.html',{'article':article})
