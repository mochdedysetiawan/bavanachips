from pyexpat import model
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Article(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='article')
    content = RichTextUploadingField(null=True)