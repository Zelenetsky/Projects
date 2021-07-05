from django.db import models

# Create your models here.
    
class UrlString(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    url_path = models.CharField(max_length=300, default="")
    
    def __str__(self):
        return self.url_path
    
    def get_absolute_url(self):
        return 'home'
        
    