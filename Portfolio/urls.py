
from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name = "main_page"),
    path('media/', views.main_page, name = "media_page"),
    path('cv/', views.cv_page, name = "cv_page"),
    path('projects/', views.projects_page, name= "projects_page"),
    path('certificates/', include('main.urls'))


]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)