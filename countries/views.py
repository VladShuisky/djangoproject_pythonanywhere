from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Country
from .serializers import CapitalSerializer


class GetCapitalInfoView(APIView):
    def get(self, request):
        queryset = Country.objects.all()
        serializer = CapitalSerializer(instance=queryset, many=True)
        return Response(serializer.data)
