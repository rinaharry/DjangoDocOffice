from django.contrib import admin
from .models import Choice,Question

class QuestionAdmin(admin.ModelAdmin):
     list_display = ("question_text","pub_date")

class ChoiceAdmin(admin.ModelAdmin):
    pass
    # list_display = ("code", "discout")
admin.site.register(Question,QuestionAdmin) 
admin.site.register(Choice,ChoiceAdmin)
