from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from voice_bot.decorators import add_bot

from .models import Task


@add_bot(bot_name='taskbot')
def task_main(request, **kwargs):
    """
    Main page with tasks
    :param request:
    :return:
    """
    user_tasks = []
    if not request.user.is_anonymous:
        user_tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_page.html', {'tasks': Task.objects.all(),
                                              'user_tasks': user_tasks,
                                              "commands": kwargs['commands'],
                                              "bot_name": kwargs['bot_name']},)


@login_required()
@api_view(['POST'])
def submit_to_task(request):
    """
    Submit to task function
    :param request: API POST request
    :return:
    """
    if request.method == 'POST':
        try:
            task_id = request.data['task_id']
            task = Task.objects.get(pk=task_id)
            task.status = request.data['status']
            task.save()
            return Response({"message": "Success"})
        except KeyError:
            return Response({"message": "Error!"})
