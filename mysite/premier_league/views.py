from django.shortcuts import render
from django import forms
from .models import Player
from thefuzz import fuzz, process
import json,math

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

matches = {'92':[1,462],'93':[463,924],'94':[925,1386],'95':[1387,1766],'96':[1767,2146],'97':[2147,2526],'98':[2527,2906],'99':[2907,3286],
           '00':[3287,3666],'01':[3667,4046],'02':[4047,4426],'03':[4427,4806],'04':[4807,5186],'05':[5187,5566],'06':[5567,5946],
           '07':[5947,6326],'08':[6327,6706],'09':[6707,7086],'10':[7087,7466],'11':[7467,7846],'12':[7864,8243],'13':[9231,9610],
           '14':[9611,9990],'15':[12115,12494],'16':[14040,14419],'17':[22342,22721],'18':[38308,38687],'19':[46605,46984],'20':[58896,59275],
           '21':[66342,66721],'22':[74911,75290]}

condition = [[7847,8226],[8227,8606],[8607,8986],[8987,9366],[9367,9746],[9747,10126],[10127,10506],[10507,10886],[10887,11266],[11267,11646],[11647,12026]]
a1 = [7864,9231,9611,12115,14040,22342,38308,46605,58896,66342,74911]
def result(request):
    real_name = request.POST.get('real_name').split(',')[0]
    try:
        info = Player.objects.get(name=real_name)
    except Player.DoesNotExist:
        info = None
    
    match_num_lst = (info.match_num_lst)
    simple_lst = list(range(1,len(info.points_lst) ))
    match_num_lst_puri=[]
    for num in match_num_lst:
        tmp_num=0
        if num >= condition[0][0] and num<=condition[0][1]:
            add_ = a1[0]-condition[0][0]
            match_num_lst_puri.append(math.floor(num + add_))


        elif num >= condition[1][0] and num<=condition[1][1]:
            add_ = a1[1]-condition[1][0]
            match_num_lst_puri.append(math.floor(num + add_))

        elif num >= condition[2][0] and num<=condition[2][1]:
            add_ = a1[2]-condition[2][0]
            match_num_lst_puri.append(math.floor(num + add_))

        elif num >= condition[3][0] and num<=condition[3][1]:
            add_ = a1[3]-condition[3][0]
            match_num_lst_puri.append(math.floor(num + add_))

        elif num >= condition[4][0] and num<=condition[4][1]:
            add_ = a1[tmp_num]-condition[tmp_num][0]
            match_num_lst_puri.append(math.floor(num + add_))
        
        elif num >= condition[5][0] and num<=condition[5][1]:
            add_ = a1[5]-condition[5][0]
            match_num_lst_puri.append(math.floor(num + add_))

        elif num >= condition[6][0] and num<=condition[6][1]:
            add_ = a1[6]-condition[6][0]
            match_num_lst_puri.append(math.floor(num + add_))

        elif num >= condition[7][0] and num<=condition[7][1]:
            add_ = a1[7]-condition[7][0]
            match_num_lst_puri.append(math.floor(num + add_))

        elif num >= condition[8][0] and num<=condition[8][1]:
            add_ = a1[8]-condition[8][0]
            match_num_lst_puri.append(math.floor(num + add_))

        elif num >= condition[9][0] and num<=condition[9][1]:
            add_ = a1[9]-condition[9][0]
            match_num_lst_puri.append(math.floor(num + add_))

        elif num >= condition[10][0] and num<=condition[10][1]:
            add_ = a1[10]-condition[10][0]
            match_num_lst_puri.append(math.floor(num + add_))
        
        else:
            match_num_lst_puri.append(math.floor(num))



    context = {'info': info,'match_num_lst':match_num_lst_puri,'simple_lst':simple_lst}
    return render(request,"player_info.html",context)
