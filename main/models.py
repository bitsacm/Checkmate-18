# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# CustomUser is the extended user model
# Create your models here

class PuzzlePc(models.Model):
	idno = models.IntegerField()
	name = models.CharField(max_length=10,default="")

	def __str__(self):
		return str(self.idno)

class UserProfile(AbstractUser):
	#user = models.OneToOneField(User)
	regTime = models.DateTimeField(null=True)
	score = models.IntegerField(default = 0)
	minesLeft = models.IntegerField(default=20)#
	#question_left = models.IntegerField(default=20)
	mines = models.CharField(max_length=144,default='192100191000129100111111012210000191001910000111123321111000199291191011232322112129921291013931239211019920921101233210110001992000000001392000')
	fieldViewed = models.CharField(max_length=144,default="hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
	puzzleRetrieved = models.ManyToManyField(PuzzlePc)
	puzzlePc = models.IntegerField(default=-1)
	currentQs=models.IntegerField(default=-1)
	questDone = models.IntegerField(default=0)
	# quesTry = models.CharField(max_length=20,default="00000000000000000000")#0=no trial 3 = 3 trials
	correctAns = models.CharField(max_length=20,default="00000000000000000000")#0=wrong 1 = correct 2=attempt
	#flag = models.ManyToManyField(flagUsed)
	#flagUsed = model.IntegerField(default=0)
	def __str__(self):
		return self.teamname





class Question(models.Model):
	questionno = models.IntegerField()
	solution = models.CharField(max_length=50)
	question = models.CharField(max_length=10000,default="")
	#puzzlePc = models.IntegerField(default=-1)#contains idno of puzzle pc associated or else -1
	row=models.IntegerField()
	col=models.IntegerField()

	def __str__(self):
		return str(self.questionno)

