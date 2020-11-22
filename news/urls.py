from django.urls import path
from .views import view_news, create_news, HomeNews, NewsByCategory

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    # path('', index, name='home'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>', view_news, name='view_news'),
    path('news/create-news/', create_news, name='create_news'),
]
