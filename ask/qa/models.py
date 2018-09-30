# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    added_at=models.DateTimeField
    rating=models.IntegerField
    author=models.ForeignKey(User)
    likes=models.ManyToManyField(User)
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

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')
