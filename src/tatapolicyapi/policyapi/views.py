from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Rest Framework Files
from rest_framework import viewsets
from .serializers import policySerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

# Data Model
from .models import data_policy


# View Logic to give data
@api_view(['GET', 'POST'])
def policy_list(request):
    if request.method == 'GET':
        snippets = data_policy.objects.all()
        print(snippets)
        serializer = policySerializers(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = policySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@csrf_exempt
def policy_list_user(request, uname):
    if request.method == 'GET':
        snippets = data_policy.objects.filter(policy_cname__contains=uname)
        print(snippets)
        serializer = policySerializers(snippets, fields=('policy_no', 'policy_cname'), many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = policySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@csrf_exempt
def policy_details(request, policy_no):

    if request.method == 'GET':
        snippets = data_policy.objects.filter(policy_no=policy_no)
        serializer = policySerializers(snippets, fields=('policy_no', 'policy_cname', 'policy_type', 'policy_start', 'policy_expire'), many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = policySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PolicyViewSet(viewsets.ModelViewSet):
    queryset = data_policy.objects.all()
    serializer_class = policySerializers
