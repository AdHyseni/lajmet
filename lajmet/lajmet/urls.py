from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('flash.urls')),
    path('redaksia/',include('redaksia.urls')),
    path('logout/', auth.LogoutView.as_view(template_name ='lajmet/index.html'), name ='logout'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )

