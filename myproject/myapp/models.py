from django.db import models

# Create your models here.
class Sret(models.Model):
    name=models.CharField(max_length=33)
    dept=models.CharField(max_length=33)
    rollno=models.IntegerField()

    def __str__(self):
        return self.name