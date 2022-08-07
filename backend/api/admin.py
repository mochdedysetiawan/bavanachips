from django.contrib import admin

# from .models import Question, Choice
from . import models

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date')
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question', 'choice_text','votes']
    list_display = ('question', 'choice_text', 'votes')
    search_fields = ['choice_text', 'votes']

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title','image','content']
    list_display = ['title']
    search_fields = ['title']

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice, ChoiceAdmin)
admin.site.register(models.Article,ArticleAdmin)