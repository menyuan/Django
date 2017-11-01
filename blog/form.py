# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import Column , Article
from django import forms
from django.forms import ModelForm
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','slug']