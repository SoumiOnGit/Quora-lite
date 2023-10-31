# core/forms.py
from django.contrib.auth.models import User 
from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']

from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
