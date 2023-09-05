from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import certificates, projects
from django.conf import settings
import os



def main_page(request):

    return render(request, "main/main.html" )


def cv_page(request):
    f = open('static/CV.txt', 'r')
    file_content = f.read()
    content = {"file_content": file_content}
    f.close()
    return render(request, 'main/CV.html', content)


def projects_page(request):
    pr_data = projects.objects.all()

    context = {"projects_data" : pr_data,
               "media_url": settings.MEDIA_URL}

    return render(request,'main/projects_page.html', context)


def certificates_page(request):
    cert_data =  certificates.objects.all()
    return render(request, "main/certificates.html",{"certificates": cert_data, "media_url": settings.MEDIA_URL},  )


def details_certificate(request, certificate_id):
    certif =  certificates.objects.all()
    return render(request, "main/details_certificate.html", {"c_id": certificate_id, "data" : certif, "media_url": settings.MEDIA_URL})
