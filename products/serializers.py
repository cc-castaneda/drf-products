from rest_framework import serializers
from .models import *
from rest_framework.decorators import api_view

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ClientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    client = ClientListSerializer()

    class Meta:
        model = Bill
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class BillProductSerializer(serializers.ModelSerializer):
    bill    = BillSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = BillProduct
        fields = ('id', 'bill', 'product')
