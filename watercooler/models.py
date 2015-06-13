from django.db import models

'''
The data model is incomplete. Possible extensions include

(1) Relating comments and questions to threads
(2) Comment threads, and comment likes
(3) Allowing only one vote per question

'''

class Thread(models.Model):
    title = models.CharField(max_length=200)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Comment(models.Model):
    text = models.CharField(max_length=400)
