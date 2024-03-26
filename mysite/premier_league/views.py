from django.shortcuts import render
from django import forms

#class SearchForm(forms.Form):
#    search = forms.CharField(label='enter player name : ', max_length=40)

# Create your views here.
def index(request):
    #context = {'example' : 1 }
    return render(request, "premier_league/index.html")

def search(request):
    search_name = request.POST.get('q')
    context = {'search_name':search_name}
    #여기에 이름 찾는 알고리즘 넣기
    return render(request, "premier_league/search_result.html", context)


