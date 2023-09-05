from django.db import models

class projects(models.Model):
    name = models.CharField(max_length = 75)
    descriprion = models.CharField(max_length=500)
    languages = models.CharField(max_length=50)
    frameworks = models.CharField(max_length=50)
    time = models.DateTimeField(auto_created=True)
    file = models.FileField("Task File", upload_to="project-files/", blank=False, null=False)
    github_link= models.URLField()

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name



class certificates(models.Model):
    course_name = models.CharField(max_length=100)
    subject =models.CharField(max_length=60)
    school = models.CharField(max_length=60)
    link = models.URLField()
    certificate_file= models.FileField(upload_to = "certificates_file")
    certicate_photo = models.ImageField(upload_to = "certificates_photo")
    mark = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural= "Certificates"

    def __str__(self):
        return self.course_name

