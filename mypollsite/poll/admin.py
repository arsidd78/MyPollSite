from django.contrib import admin
from .models import Question,Choices

# Register your models here.
class ChoiceModel(admin.TabularInline):
    model = Choices
    extra = 2
class QuestionModel(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question']}),

    ]
    search_fields = ['question']
    inlines = [ChoiceModel]

admin.site.register(Question,QuestionModel)

