from django import forms
from .models import Answer, Question

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['nick', 'content']
        widgets = {
            'nick': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Twój nick'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Twoja błyskotliwa odpowiedź...'}),
        }
        labels = {
            'nick': '',
            'content': '',
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Np. Co by było, gdyby niebo było zielone?'}),
        }
        labels = {
            'text': 'Treść Twojego pytania',
        }