from django.urls import path
from main import views
urlpatterns = [
    
    path('article/<int:pk>',views.article, name='get_article'),
    path('author/<int:pk>',views.author, name='get_author'),
    path('',views.index, name='index'),
    path('article',views.create_article, name='create_article'),
]