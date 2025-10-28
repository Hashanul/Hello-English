from rest_framework import serializers
from .models import Banner


class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

    

