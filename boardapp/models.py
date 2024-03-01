from django.db import models

class BoardModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.CharField(max_length = 50)
    snsimage = models.ImageField('')
    good = models.IntegerField(null=True,blank=True,default=1)
    read = models.IntegerField(null=True,blank=True,default=1)
    read_text = models.TextField(null=True,blank=True,default='a')



