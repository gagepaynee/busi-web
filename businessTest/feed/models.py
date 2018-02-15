from django.db import models
from django.utils import timezone
from vote.models import VoteModel
# Create your models here.



"""class Article(models.Model):
    networks = models.ManyToManyField(Network, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    network1_name = models.CharField(max_length=100, blank=True, null=True)
    network1_link = models.URLField(blank=True, null=True) 
    network1_likes = models.IntegerField(default=0)
    network1_dislikes = models.IntegerField(default=0)
    network2_name = models.CharField(max_length=100, blank=True, null=True)
    network2_link = models.URLField(blank=True, null=True) 
    network2_likes = models.IntegerField(default=0)
    network2_dislikes = models.IntegerField(default=0)
    network3_name = models.CharField(max_length=100, blank=True, null=True)
    network3_link = models.URLField(blank=True, null=True)
    network3_likes = models.IntegerField(default=0)
    network3_dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title"""

class Article(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Network(VoteModel, models.Model):
    article = models.ForeignKey(Article, blank=True)
    name = models.CharField(max_length=100, default='', blank=True)
    link = models.URLField(default='', blank=True)
    likes2 = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name
class Likes(models.Model):
    mynetwork = models.ForeignKey(Network)
    created = models.DateTimeField(auto_now_add=True)