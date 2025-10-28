from django.shortcuts import render
from rest_framework import viewsets
from .models import Banner
from .serializers import BannerSerializers


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializers
