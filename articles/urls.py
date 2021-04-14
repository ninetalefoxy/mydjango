from django.urls import path
from django.conf.urls import url
from . import views
from .models import Article

urlpatterns = [
    url(r'^$', views.article_list),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail),
]


