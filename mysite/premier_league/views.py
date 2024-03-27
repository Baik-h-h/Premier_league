from django.shortcuts import render
from django import forms
from .models import Player
from thefuzz import fuzz, process

def name_per(check_name):
    players = Player.objects.all()  # 이 부분을 함수 내로 이동하여 모델을 가져옵니다.
    names = players.values_list('name', flat=True)  # 플레이어 이름만 가져옵니다.
    check_name = check_name.lower()
    return_dict = {}
    
    for i, name in enumerate(names):
        per = fuzz.token_sort_ratio(check_name, name.lower())
        if per == 100:
            return {i: per}
        elif per >= 70:
            return_dict[i] = per
    
    return_dict = sorted(return_dict.items(), key=lambda x: x[1], reverse=True)
    if len(return_dict) > 5:
        return_dict = return_dict[:5]
    
    return dict(return_dict)

def index(request):
    return render(request, "index.html")

def search(request):
    if request.method == 'POST':
        search_name = request.POST.get('q')
        name_dict = {}
        for k, v in name_per(search_name).items():
            #print(k,v)
            player = Player.objects.get(pk=k+1)
            name_dict[player.name] = v
        context = {'name_dict': name_dict, 'input_name':search_name}
        return render(request, "search_result.html", context)
    else:
        return render(request, "search_result.html", {})

def result(request):
    real_name = request.POST.get('real_name').split(',')[0]
    try:
        info = Player.objects.get(name=real_name)
    except Player.DoesNotExist:
        info = None
    context = {'info': info}
    return render(request,"player_info.html",context)