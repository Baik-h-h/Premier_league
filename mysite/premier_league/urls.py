from django.urls import path

from . import views

app_name = "premier_league"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("result/", views.result, name="result"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
]