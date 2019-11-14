from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="djan"
urlpatterns=[
    path('',views.indexpage,name='index'),
    path('register/',views.register,name='register'),
    path('family/',views.family,name='family'),
    path('income/',views.income,name='income'),
    path('expenditure/',views.expenditure,name='expenditure'),
    path('liability/',views.liability,name='liability'),
    path('savings/',views.savings,name='savings')
]
urlpatterns += staticfiles_urlpatterns()