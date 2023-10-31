# core/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question_form.html'
    success_url = reverse_lazy('question_list')

@login_required
def answer_create_view(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
    return redirect('question_detail', pk=question.id)

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
        else:
            error_message = "Invalid username or password. Please try again."
    return render(request, 'registration/login.html', {'error_message': error_message})

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm
from .models import Question
from django.contrib.auth import login, logout


@login_required
def post_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = AnswerForm()

    return render(request, 'post_answer.html', {'form': form, 'question': question})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout
