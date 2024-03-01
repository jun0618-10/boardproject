
from django.contrib import admin
from django.urls import path,include
from .views import signupfunc,loginfunc,listfunc,logoutfunc,ditailfunc,goodfunc,readfunc,BoardCreate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup/", signupfunc,name='signup'),
    path('login/',loginfunc,name='login'),
    path('list/',listfunc,name='list'),
    path('logout/',logoutfunc,name='logout'),
    path('ditail/<int:pk>',ditailfunc,name='ditail'),
    path('good/<int:pk>',goodfunc,name='good'),
    path('read/<int:pk>',readfunc,name='read'),
    path('create/',BoardCreate.as_view(),name='create'),
    


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

