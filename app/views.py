from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def task_list(request):
    if request.method=='GET':
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=TaskSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        

@api_view(['GET','PUT','DELETE'])
def task_detail(request,pk):
    try:
        task=Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error":"task id not found"})
    if request.method=='GET':
        serializer=TaskSerializer(task)
        return Response(serializer.data)
    if request.method=='PUT':
        serializer=TaskSerializer(task,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
    if request.method=='DELETE':
        task.delete()
        return Response({"message":"id delete successfully"})