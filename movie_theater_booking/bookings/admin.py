# Register your models here.
from django.contrib import admin
from django.db import models
from .models import Movie, Seat, Booking, Question
from .models import Choice, Question

#admin.site.register(Question, QuestionAdmin,)
admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Booking)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_display = ["question_text", "pub_date", "was_published_recently"]


admin.site.register(Question, QuestionAdmin)









