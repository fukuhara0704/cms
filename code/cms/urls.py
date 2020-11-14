from django.urls import path
from . import views

app_name = 'cms'
# 各viewへのルーティング
urlpatterns = [
    # 顧客一覧画面面
    path('', views.MemberList.as_view(), name='member_list'),
    # 顧客情報詳細画面
    path('<int:pk>/', views.MemberDetail.as_view(), name='detail'),
    # 新規顧客登録画面
    path('create/', views.form, name='create'),
    # 顧客情報編集画面
    path('<int:pk>/update/', views.MemberUpdate.as_view(), name='update'),
    # 削除確認画面
    path('<int:pk>/delete/', views.MemberDelete.as_view(), name='delete'),
    #
    #path('regist/', views.MenuRegist.as_view(), name='regist'),
    # 注文登録画面
    # path('regist/', views.order_form, name='ajax_search'),
    path('regist/', views.OrderRegistList.as_view(), name='ajax_search'),
    # 非同期　会員情報取得取得
    #path('regist/search/', views.ajax_post_search, name='ajax_post_search'),
    path('regist/search', views.ajax_post_search, name='ajax_post_search'),
    #
    #path('regist/search/', views.OrderCreate.as_view(), name='ajax_post_search'),
    # 非同期 カテゴリ、商品名取得処理
    path('regist/goods/', views.ajax_get_goods, name='ajax_get_goods'),
    #
    #path('regist/create/', views.RegistOrder.as_view(), name='create_order'),
]