from django.db import models
from bs4 import BeautifulSoup

# Create your models here.
    
class UrlString(models.Model):
    url_path = models.CharField(max_length=300, default='')

    def count_tags(self):
        # {'values': [["<html>", 5], ["<head>", 8], ["<p>", 1], ["<div>", 1]]}
        resulting_dictionary = {'values':[]}
        
        soup=BeautifulSoup(self.url_path, 'html.parser')
        html_find = soup.find_all('<html>')
        head_find = soup.find_all('<head>')
        p_find = soup.find_all('<p>')
        div_find = soup.find_all('<div>')
        resulting_dictionary['values'] = [["<html>", len(html_find)], ["<head>", len(head_find)], ["<p>", len(p_find)], ["<div>", len(div_find)]]

        return resulting_dictionary

    def __str__(self):
        return self.count_tags()
    
    def get_absolute_url(self):
        return 'home'
        
    