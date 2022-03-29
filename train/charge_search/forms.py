from django import forms
from .models import *


class SearchForm(forms.Form):
    line = forms.CharField(max_length=100, widget=forms.HiddenInput())

    input_dep = forms.CharField(label="乗車駅", max_length=20, widget=forms.TextInput(
        attrs={'placeholder': '駅名'}))
    input_arr = forms.CharField(label="降車駅", max_length=20, widget=forms.TextInput(
        attrs={'placeholder': '駅名'}))

    def clean_input_dep(self):
        input_dep = self.cleaned_data['input_dep']
        line = self.cleaned_data['line']

        if input_dep == ('伊豆高原'or'伊豆熱川'or'伊豆稲取'or'河津'or'伊豆急下田'or'三島'or'三島田町'or'大場'or'伊豆長岡'or'大仁'or'修善寺'):
            raise forms.ValidationError("伊東〜伊豆急下田間・熱海〜修善寺間を含む区間の検索はできません")

        if not eval(line+"StationModel").objects.filter(sta_name=input_dep):
            raise forms.ValidationError("乗車駅の入力に誤りがあります。")
        return input_dep

    def clean_input_arr(self):
        input_arr = self.cleaned_data['input_arr']
        line = self.cleaned_data['line']

        if input_arr == ('伊豆高原'or'伊豆熱川'or'伊豆稲取'or'河津'or'伊豆急下田'or'三島'or'三島田町'or'大場'or'伊豆長岡'or'大仁'or'修善寺'):
            raise forms.ValidationError("伊東〜伊豆急下田間・熱海〜修善寺間を含む区間の検索はできません")

        if not eval(line+"StationModel").objects.filter(sta_name=input_arr):
            raise forms.ValidationError("降車駅の入力に誤りがあります。")
        return input_arr

    def clean(self):
        cleaned_data = super().clean()
        input_dep = cleaned_data.get('input_dep')
        input_arr = cleaned_data.get('input_arr')
        line = cleaned_data.get('line')
        try:
            input_dep_obj = eval(line+"StationModel").objects.filter(sta_name=input_dep)[0]
            input_arr_obj = eval(line+"StationModel").objects.filter(sta_name=input_arr)[0]

            if input_dep_obj.branch != input_arr_obj.branch:
                raise forms.ValidationError("折返しとなる経路です。この経路では検索できません。")
        except IndexError:
            pass
        
        if input_dep == input_arr and (input_dep or input_arr) is not None:
            raise forms.ValidationError("乗車駅と降車駅が同じ駅です。")

        return self.cleaned_data
