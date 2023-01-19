from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [ 
        path('', views.StartingPage.as_view(), name ='index'),
        path('login/', views.Login, name ='login'),
        path('register/', views.register, name ='register'),
        path('lajmet/', views.lajmet_e_mia, name ='lajmet-e-mia'),
        path('krijo/', views.krijo, name ='krijo'),
        path('lajmi/<slug:slug>', views.lajmi, name ='lajmi-redaksia'),
        path('update/<slug>',views.perditeso,name='update'),
        path('delete/<slug:slug>',views.fshij,name='fshij'),

    ]