from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [ 
        path('', views.index, name ='index'),
        path('login/', views.Login, name ='login'),
        path('register/', views.register, name ='register'),
        path('lajmet/', views.lajmet_e_mia, name ='lajmet-e-mia'),
        path('redakto/', views.redakto, name ='redakto'),

    ]