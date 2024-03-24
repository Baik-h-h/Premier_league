from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'example' : 1 }
    return render(request, "premier_league/index.html", context)