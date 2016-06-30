from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class FacebookModel(models.Model):
    name = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=10000, blank=True, default='')
    start_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000, blank=True, default='')
    source =  models.CharField(max_length=100, blank=True, default='')
    #image = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    #class Meta:
        #ordering = ('created',)
