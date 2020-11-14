from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import Member
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from .models import Book

def index(request):
    param = {"message": "crud_appです"}
    return render(request, 'crud_app/index.html', param)


def hello(request):
    return HttpResponse("<H1>hello</H1>")

def new(request):
    params = {'name': '', 'email': '', 'form': None}
    if request.method == 'POST':
        form = UserForm(request.POST)
        params['name'] = request.POST['name']
        params['email'] = request.POST['email']
        params['form'] = form
    else:
        params['form'] = UserForm()
    return render(request, 'crud_app/new.html', params)

class MemberList(ListView):
    # context_object_name = 'member_list'
    model = Member
    # paginate_by = 3
    # queryset = Member.objects.all()
    # queryset = Member.objects.order_by('-age')
    # queryset = Member.objects.filter(age='11')

class MemberDetail(DetailView):
    template_name = 'crud_app/member_detail.html'
    model = Member

class MemberCreate(CreateView):
    template_name = 'crud_app/member_form.html'
    model = Member
    fields = ['name', 'nickname', 'age']

    def get_success_url(self):
        return reverse('crud_app:detail', kwargs={'pk': self.object.pk})

class MemberUpdate(UpdateView):
    template_name = 'crud_app/member_update_form.html'
    model = Member
    fields = ['name', 'nickname', 'age']

    def get_success_url(self):
        return reverse('crud_app:detail', kwargs={'pk': self.object.pk})

    def get_form(self):
        form = super(MemberUpdate, self).get_form()
        form.fields['name'].label = '名前'
        form.fields['nickname'].label = 'ニックネーム'
        form.fields['age'].label = '年齢'
        return form

class MemberDelete(DeleteView):
    template_name = 'crud_app/member_confirm_delete.html'
    model = Member

    success_url = reverse_lazy('crud_app:member')

class BookList(ListView):
     def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Book.objects.filter(
                Q(title__icontains=q_word) | Q(author__icontains=q_word))
        else:
            object_list = Book.objects.all()
        return object_list