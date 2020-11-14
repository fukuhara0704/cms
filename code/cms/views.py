from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from .models import Member,Order,Drink,Course,MenuCategory,Goods
from .forms import MemberForm,DrinkForm
import datetime
from django.http import JsonResponse

# 顧客一覧画面
class MemberList(ListView):
    context_object_name = 'members'
    template_name = 'cms/member_list.html'
    model = Member

    # カテゴリ取得
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        goods_list = Goods.objects.all()
        context['goods_list'] = goods_list
        return context

    def get_queryset(self):
        q_name = self.request.GET.get('name')
        q_name_read = self.request.GET.get('nameRead')
        q_age = self.request.GET.getlist('age')
        q_visit_num = self.request.GET.getlist('visitNum')
        q_latest_visit_day = self.request.GET.get('latestVisitDay')

        # 検索条件の場合分け
        object_list = Member.objects.all()
        # 名前、連絡先、住所、年齢
        if q_name:
            object_list = object_list.filter(Q(name__icontains=q_name))
        if q_name_read:
            object_list = object_list.filter(Q(name_read__icontains=q_name_read))
        if q_age:
            queries = [Q(age__range=(age, str(int(age)+ 9))) for age in q_age]
            query = queries.pop()
            for item in queries:

                query |= item

            object_list = object_list.filter(query)
        if q_visit_num:
            queries = [Q(visit_num=visit_num) for visit_num in q_visit_num]
            query = queries.pop()
            for item in queries:

                query |= item

            object_list = object_list.filter(query)
        if q_latest_visit_day:
            d_latst_visit_day = datetime.datetime.strptime(q_latest_visit_day, '%Y-%m-%d')
            object_list = object_list.filter(Q(latest_visit_day=d_latst_visit_day))

        return object_list

# 顧客情報詳細画面
class MemberDetail(DetailView):
    context_object_name = 'member'
    template_name = 'cms/member_detail.html'
    model = Member
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_list = Order.objects.filter(member_id=self.kwargs['pk'])
        #order_list = Drink.objects.filter(order__member_id=self.kwargs['pk'] )
        context['order_list'] = order_list
        # Orderの
        drink_list = Drink.objects.filter(order__member_id=self.kwargs['pk'])
        context['drink_list'] = drink_list
        return context

# 新規顧客登録画面
def form(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            return redirect('cms:member_list')
    else:
        form = MemberForm()
    return render(request, 'cms/member_form.html' ,{'form': form})

# 顧客情報編集画面
class MemberUpdate(UpdateView):
    template_name = 'cms/member_update_form.html'
    model = Member
    fields = ['name', 'name_read', 'age']

    def get_success_url(self):
        return reverse('cms:detail', kwargs={'pk': self.object.pk})

    def get_form(self):
        form = super(MemberUpdate, self).get_form()
        form.fields['name'].label = '名前'
        form.fields['name_read'].label = 'フリガナ'
        form.fields['age'].label = '年齢'
        return form

# 削除確認画面
class MemberDelete(DeleteView):
    template_name = 'cms/member_confirm_delete.html'
    model = Member
    success_url = reverse_lazy('cms:member_list')

def createOrder(request):
    template_name = 'cms/order_regist.html'


# 注文登録画面
# def order_form(request):
#     print('start')
#     if request.method == 'POST':
#         # リクエストがPOSTの時
#         print('POST')
#         form = DrinkForm(request.POST)
#         if form.is_valid():
#             member = form.save(commit=False)
#             member.save()
#             # 登録成功したら、顧客一覧画面へ遷移
#             return redirect('cms:member_list')
#     else:
#         # POST以外の時
#         print('POST以外')
#         form = DrinkForm()
#         template_name = 'cms/menu_regist.html'
#         model = MenuCategory
#         print('get_context_data前')
#         def get_context_data(self, **kwargs):
#             print('get_context_data start')
#             context = super().get_context_data(**kwargs)
#             category_list = MenuCategory.objects.all()
#             context['category_list'] = category_list
#             print(context)
#             return context
#     print('return前')
#     return render(request, 'cms/menu_regist.html' ,{'form': form })

# 注文登録画面
class OrderRegistList(ListView):
    template_name = 'cms/menu_regist.html'
    model = MenuCategory
    print('get_context_data前')
    def get_context_data(self, **kwargs):
        print('get_context_data中')
        context = super().get_context_data(**kwargs)
        category_list = MenuCategory.objects.all()
        context['category_list'] = category_list
        print('get_context_data後')
        return context

class OrderCreate(CreateView):
    template_name = 'cms/menu_regist.html'
    model = Member
    fields = ['name', 'name_read', 'age']

# 非同期 カテゴリ、商品名取得処理
def ajax_post_search(request):
    keyword = request.GET.get('name')
    if keyword:
        member = [{"name" :member.name,"id" : member.id} for member in Member.objects.filter(name__icontains=keyword)]  # タイトルにキーワードを含む。大文字小文字の区別なし
    else:
        member = [{"name" :member.name,"id" : member.id} for member in Member.objects.all()]
    d = {
        "member": member
    }
    return JsonResponse(d)

# 非同期　会員情報取得取得
def ajax_get_goods(request):
    category_id = request.GET.get('category_id')

    if category_id:
        goods = [{"category_id" : goods.category.pk, "category_name" : goods.category.category_name, "goods_id" : goods.pk, "goods_name" : goods.goods_name}
        for goods in Goods.objects.filter(category_id=category_id)]
    d = {
        "goods": goods
    }
    return JsonResponse(d)