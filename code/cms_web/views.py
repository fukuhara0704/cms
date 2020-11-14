from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import MemberInfo
from django.urls import reverse
# from .forms import MemberForm

def index(request):
    return render(request, 'cms_web/index.html')

def search(request):
    return render(request, 'cms_web/search.html')

def regist(request):
    return render(request, 'cms_web/regist.html')

class RegistListView(ListView):
    model = MemberInfo
    template_name = "regist.html"

class UserListView(ListView):
    model = MemberInfo
    template_name = "cms_web/list.html"

class MemberDetail(DetailView):
    model = MemberInfo
    template_name = "cms_web/member_list.html"

"""
def new(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = MemberForm()
    return render(request, 'cms_web/regist.html', params)
"""

def list(request):
    data = MemberInfo.objects.all()
    params = {'message': 'メンバーの一覧', 'data': data}
    return render(request, 'cms_web/list.html', params)
