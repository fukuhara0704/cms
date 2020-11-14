from django import forms
from .models import Member,Drink


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
         # 1) 元から Model にある属性を hidden にしたい場合
        #widgets = {'__all__': forms.HiddenInput()}


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = '__all__'
