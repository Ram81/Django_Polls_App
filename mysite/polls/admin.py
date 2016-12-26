from django.contrib import admin
from .models import Question,choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
	model=choice
	extra=3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets=[
		(None,{'fields' :['question_text']}),
		('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
	]
	inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmin)


