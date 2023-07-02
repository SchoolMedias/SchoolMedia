from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
# Create your views here.

@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = request.GET.get('book_name')
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


class DataTest(APIView):
    def get(self,request,*args,**kwargs):
        print('请求后台数据成功！')
        return Response(['后台列表数据1','后台列表数据2'])



class Search(APIView):
    def get(self,request):
        kw = request.GET.get('0', None)
        print(request.GET.get('0', None))
        if kw != None:
            return Response("您搜索的数据为：" + kw)
        else:
            return Response("没有搜索到任何数据")

