from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="djan"
urlpatterns=[
    path('',views.indexpage,name='index'),
    path('register/',views.register,name='register'),
    path('family/',views.family,name='family'),
    path('family/income/',views.income,name='income'),
    path('family/income/incomed/',views.incomed,name='incomed'),
    path('family/income/incomed/incomedview/',views.incomedv,name='incomedv'),
    path('family/income/incomed/incomedv/',views.incomedv,name='incomedv'),
    path('family/income/incomed/incomedv/modincome/incomedview/',views.incomedv,name='incomedv'),
    path('family/income/incomedv/modincome/',views.modincome,name='modincome'),
    path('family/income/incomedv/modincome/deleteincome/<incomeid>/',views.deleteincome,name='deleteincome'),
    path('family/income/incomedv/modincome/deleteincome/<incomeid>/income/',views.incomedv,name='incomedv'),
    path('family/income/incomedv/modincome/editincome/',views.editincome,name='editincome'),
    path('family/income/incomedv/',views.incomedv,name='incomedv'),
    path('family/income/modincome/',views.modincome,name='modincome'),
    path('family/income/incomed/incomedv/modincome/',views.modincome,name='modincome'),
    path('family/expenditure/',views.expenditure,name='expenditure'),
    path('family/expenditure/expendetail/exmodify/',views.exmodify,name='exmodify'),
    path('family/expenditure/expendetail/',views.expendetail,name='expendetail'),
    path('family/expenditure/expenditure/',views.expenditure,name='expenditure'),
    path('family/expenditure/expenditure/expendetail/',views.expendetail,name='expendetail'),
    path('liability/',views.liability,name='liability'),
    path('family/savings/',views.savings,name='savings')
]
urlpatterns += staticfiles_urlpatterns()