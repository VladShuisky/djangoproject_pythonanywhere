from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer, ApiSnippetSerializer

# @api_view(['GET', 'POST'])
class GetSnippetsView(APIView):

    def get(self, request):
        if request.method == 'GET':
            queryset = Snippet.objects.all()
            serializer = SnippetSerializer(instance=queryset, many=True)
            print(serializer.data)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = SnippetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'DELETE', 'PUT'])
class SnippetDetail(APIView):

    def get(self, request, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = SnippetSerializer(snippet)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = SnippetSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            snippet.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)


