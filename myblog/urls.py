"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from DjangoUeditor import urls
from blog import views as blog_views
urlpatterns = [
    url(r'^$', blog_views.index, name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', blog_views.column_detail, name='column'),
    url(r'^article/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', blog_views.article_detail, name='article'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL,document_root=settings.MEDIA_ROOT
    )
