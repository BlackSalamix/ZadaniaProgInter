import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
def index(request):
    return render(request, 'taskboard/index.html')
@csrf_exempt
def api_tasks(request):
    if request.method == 'GET':
        tasks = list(Task.objects.values('id', 'title', 'completed'))
        return JsonResponse({'tasks': tasks})
    elif request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(title=data['title'])
        return JsonResponse({'id': task.id, 'title': task.title, 'completed': task.completed})
@csrf_exempt
def api_task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)
    if request.method == 'PATCH':
        data = json.loads(request.body)
        if 'completed' in data:
            task.completed = data['completed']
            task.save()
        return JsonResponse({'status': 'success'})
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'status': 'deleted'})