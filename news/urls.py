from django.urls import path
from django.views.decorators.cache import cache_page
# Импортируем созданное нами представление
from .views import *


urlpatterns = [
    path('news/', cache_page(60)(NewsList.as_view()), name='news_list'),
    path('news/<int:pk>', NewsDetail.as_view(), name='post_details'),
    path('news/search/', PostSearch.as_view(), name='post_search'),
    path('news/create', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit', NewsUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete', NewsDelete.as_view(), name='news_delete'),
    path('article/create', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit', ArticleUpdate.as_view(), name='article_edit'),
    path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]
