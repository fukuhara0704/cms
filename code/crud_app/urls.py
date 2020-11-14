from django.urls import path
from . import views

app_name = 'crud_app'
urlpatterns = [
    path('new/', views.new, name='new'),
    path('', views.MemberList.as_view(), name='member'),
    path('<int:pk>/', views.MemberDetail.as_view(), name='detail'),
    path('create/', views.MemberCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.MemberUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.MemberDelete.as_view(), name='delete'),
    path('search/', views.BookList.as_view(), name='book'),
]