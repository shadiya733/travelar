from django.db import models

# Create your models here.
class regform(models.Model):
    username=models.CharField(max_length=250)
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.EmailField()
    password=models.CharField(max_length=250)



    def __str__(self):
        return self.username