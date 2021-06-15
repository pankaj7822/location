from django.db import models

# Create your models here.
class Location(models.Model):
    id=models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ip=models.CharField(max_length=300,blank=True,null=True)
    gps=models.URLField(max_length=200,blank=True,null=True)
    def __str__(self):
            return self.created_at