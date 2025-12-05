from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Count
from .models import Question, Answer
from .forms import AnswerForm, QuestionForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from .forms import QuestionForm
from django.db.models import Max
def daily_index(request):
    today = timezone.now().date()
    
    question = Question.objects.filter(used_date=today).first()

    if not question:
        available = Question.objects.filter(is_approved=True, used_date__isnull=True)
        
        if available.exists():
            question = available.order_by('?').first()
            question.used_date = today
            question.save()
        else:
            return render(request, 'daily_quiz/no_questions.html')

    sort_option = request.GET.get('sort', 'best')
    
    if sort_option == 'new':
        answers = question.answers.all().order_by('-created_at')
    else:
        answers = question.answers.all().order_by('-likes_count')
    max_likes = 0
    if answers.exists():
        max_likes = answers.aggregate(Max('likes_count'))['likes_count__max']
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.question = question
            new_answer.save()
            return redirect('daily_index')
    else:
        form = AnswerForm()
    liked_answers_ids = request.session.get('liked_answers', [])
    context = {
        'question': question,
        'answers': answers,
        'form': form,
        'today_date': today,
        'liked_answers_ids': liked_answers_ids,
        'max_likes': max_likes,
        'current_sort': sort_option,
    }
    return render(request, 'daily_quiz/index.html', context)


def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.is_approved = False
            question.save()
            return render(request, 'daily_quiz/question_submitted.html')
    else:
        form = QuestionForm()
    
    return render(request, 'daily_quiz/add_question.html', {'form': form})

@require_POST
def like_answer(request, answer_id):
    liked_answers = request.session.get('liked_answers', [])
    answer = get_object_or_404(Answer, id=answer_id)
    
    action = ''

    if answer_id in liked_answers:
        answer.likes_count -= 1
        liked_answers.remove(answer_id)
        action = 'unliked'
    else:
        answer.likes_count += 1
        liked_answers.append(answer_id)
        action = 'liked'

    answer.save()
    request.session['liked_answers'] = liked_answers
    
    return JsonResponse({
        'likes': answer.likes_count, 
        'action': action
    })