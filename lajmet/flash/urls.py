from django.urls import path
from . import views
urlpatterns = [
   path('',views.faqa_pare,name='faqa-pare'),  
   path('kontaktet/',views.kontaktet,name='kontaktet'),  
   path('ne/',views.mbi_ne,name='ne'),
   path('lajmet/',views.lajmet, name='lajmet'),
   path('lajmi/<slug:slug>',views.lajmi,name='lajmi'),  


]