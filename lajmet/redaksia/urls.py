from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [ 
        path('', views.StartingPage.as_view(), name ='index'),
        path('login/', views.Login, name ='login'),
        path('register/', views.register, name ='register'),
        path('lajmet/', views.lajmet_e_mia, name ='lajmet-e-mia'),
        path('redakto/', views.redakto, name ='redakto'),
        #path('lajmi/<int:id>', views.redakto, name ='lajmi-redaksia'),
        # path('update/<int:id>',views.update,name='update'),
        # path('delete/<int:id>',views.delete,name='delete'),

    ]