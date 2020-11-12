from django.urls import path
from .views import index, get_category, view_news, create_news

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    path('news/<int:news_id>', view_news, name='view_news'),
    path('news/create-news/', create_news, name='create_news'),
]
