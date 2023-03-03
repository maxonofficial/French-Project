from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .. import serializers,models


@api_view(['GET'])
def dept_word(request, pk):
    dept = get_object_or_404(models.department, pk=pk)
    words = models.word.objects.filter(department=dept)
    serializer = serializers.Word(words, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def word(request):
    if(request.method == 'POST'):
        word_serializer = serializers.Word(data=request.data)
        if word_serializer.is_valid():
            word_serializer.save()
            return Response(word_serializer.data, status=status.HTTP_201_CREATED)
        return Response(word_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    words = models.word.objects.all()
    serializer = serializers.Word(words,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def word_detail(request, pk):
    word = get_object_or_404(models.word, pk=pk)
    if request.method == 'GET':
        serializer = serializers.Word(word)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.Word(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

