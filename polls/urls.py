from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import  views

app_name  = 'polls'
urlpatterns = [
    # url('polls/index/',views.index,name="index"),
    # url('polls/detail/(\w+)/',views.detail,name="detail"),
    # url('polls/results/(\w+)/',views.results,name= "results"),
    # url('vote/(\w+)',views.vote,name="vote"),
# ex: /polls/
    path('index/', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
