from django.urls import path

from . import views

app_name = 'cms_web'
urlpatterns = [
    path('', views.index, name='index'),
    # path('regist/', views.regist, name='regist'),
    # path('list/', views.UserListView.as_view(), name='list'),
    path('search/', views.search, name='search'),
    path('list/<int:pk>/', views.MemberDetail.as_view(), name='detail'),
   # path('regist/', views.new, name='regist'),
    path('list/', views.list, name='list'),
]

