from django.contrib import admin
from .models import Question, Answer

@admin.action(description='Zatwierdź wybrane pytania')
def approve_questions(modeladmin, request, queryset):
    queryset.update(is_approved=True)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_approved', 'used_date', 'created_at')
    list_filter = ('is_approved', 'used_date')
    actions = [approve_questions]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('nick', 'content', 'likes_count', 'created_at')
    list_filter = ('created_at',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)