from rest_framework import serializers
from .models import *


class Itemserializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'



class Useserilizer(serializers.ModelSerializer):
    class Meta:
        model=Userr
        fields='__all__'

class Bidserializer(serializers.ModelSerializer):
    class Meta:
        model=Bids
        fields='__all__'