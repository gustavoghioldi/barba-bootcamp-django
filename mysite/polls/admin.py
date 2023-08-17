from django.contrib import admin
from polls.models import Choice, Question
# Register your models here.

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["question", "choice_text", "votes", "is_big"]
    list_filter = ["votes"]
    search_fields = ["question__question_text", "votes", "choice_text"]
    
    def is_big(self, option):
        return True if option.votes > 5 else False

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
@admin.register(Question)
class QuestioAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        ("Preguntita", {"fields": ["question_text"]}),
        ("Dia de publicacion", {"fields": ["pub_date"]}),
    ]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    inlines = [ChoiceInline]