from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.name


class Blogs(models.Model):
    id=models.CharField(max_length=20, primary_key=True)
    writer=models.CharField(max_length=122)
    read_time=models.CharField(max_length=50)
    content=models.CharField(max_length=100000)
    title=models.CharField(max_length=1000)
    # pdf = models.FileField(upload_to='pdf')
    # title_image = models.ImageField(null=True, upload_to="mansimehndiratta/images")
    def __str__(self):
        return self.id


class Title_img_upload(models.Model):
    img_upload = models.ImageField(null=True, upload_to="mansimehndiratta/images")



