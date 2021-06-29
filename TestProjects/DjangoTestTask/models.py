from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class UrlData(models.Model):
    html_num = models.IntegerField(default=0)
    head_num = models.IntegerField(default=0)
    p_num = models.IntegerField(default=0)
    div_num = models.IntegerField(default=0)

    def __str__(self):
        return "html: "+str(self.html_num)+" head: "+str(self.head_num)+" p: "+ str(self.p_num)+" div: "+str(self.div_num) 
    
    def get_absolute_url(self):
        return 'home'
    
class UrlString(models.Model):
    url_path = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.url_path
    
    def get_absolute_url(self):
        return 'home'
        
    