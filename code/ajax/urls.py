from django.urls import path
from . import views

app_name = 'ajax'
urlpatterns = [
    path('', views.PostList.as_view(), name='ajax_post_add'),
    path('add/', views.ajax_post_add, name='ajax_post_add'),
    path('search/', views.ajax_post_search, name='ajax_post_search'),
]