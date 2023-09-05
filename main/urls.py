from django.urls import path
from . import views

urlpatterns = [
    path('', views.certificates_page, name= "certificates_page"),
    path('<int:certificate_id>/', views.details_certificate),
]