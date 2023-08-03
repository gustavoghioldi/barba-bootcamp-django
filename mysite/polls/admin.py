from django.contrib import admin
from polls.models import Choice, Question
# Register your models here.

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestioAdmin(admin.ModelAdmin):
    pass
