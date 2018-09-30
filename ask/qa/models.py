# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')
# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    added_at=models.DateTimeField(blank = True, auto_now_add=True)
    rating=models.IntegerField(default=0)
    author=models.ForeignKey(User)
    likes=models.ManyToManyField(User, blank = True, null = True,related_name='likes_set')
    objects=QuestionManager()
    def __unicode__(self):
        return self.title
#    def get_absolute_url(self):
#        return

class Answer(models.Model):
    text=models.TextField()
    added_at=models.DateTimeField()
    question=models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author=models.ForeignKey(User)


