from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .. import serializers,models

@api_view(['GET','POST'])
def dept(request):
    if(request.method == 'POST'):
        dept_serializer = serializers.Department(data=request.data)
        if dept_serializer.is_valid():
            dept_serializer.save()
            return Response(dept_serializer.data, status=status.HTTP_201_CREATED)
        return Response(dept_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    depts = models.department.objects.all()
    serializer = serializers.Department(depts,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def dept_detail(request, pk):
    dept = get_object_or_404(models.department, pk=pk)
    if request.method == 'GET':
        serializer = serializers.Department(dept)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.Department(dept, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dept.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

