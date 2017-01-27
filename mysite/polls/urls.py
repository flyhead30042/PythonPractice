from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/all/$', views.all_question, name='all_question'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name='question'),
    url(r'^question_detail/(?P<question_id>[0-9]+)/$', views.question_detail, name='question_detail'),
]