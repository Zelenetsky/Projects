from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class UrlData(models.Model):
    html_num = IntegerField(default=0)
    head_num = IntegerField(default=0)
    p_num = IntegerField(default=0)
    div_num = IntegerField(default=0)

    def __str__(self):
        return "html: "+ self.html_num + "\nhead: "+ self.head_num + "\np: "+ self.p_num + "\ndiv: "+ self.div_num 
    
    def get_absolute_url(self):
        return ''
    