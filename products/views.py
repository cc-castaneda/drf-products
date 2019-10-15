from django.shortcuts import render
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import (DjangoModelPermissions)
import csv
from django.http import HttpResponse
from .serializers import *
from .models import *


@api_view(['GET', 'POST'])
def bill_product_list(request):
    if request.method == 'GET':
        bill_product = BillProduct.objects.all()
        serializer   = BillProductSerializer( bill_product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BillProductSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def bill_product_detail(request, pk):
    try:
        bill_product = BillProduct.objects.get(pk=pk)
    except BillProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BillProductSerializer(bill_product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BillProductSerializer(bill_product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bill_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def BillProductCSVExport(request, pk):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Bill product data.csv"'

    writer = csv.writer(response)

    bill_product =  BillProduct.objects.get(pk=pk)

    writer.writerow(['COMPANY_NAME', 'NIT', 'CODE',])
    writer.writerow([bill_product.bill.company_name,
                        bill_product.bill.nit,
                        bill_product.bill.code]
                        )
    return response