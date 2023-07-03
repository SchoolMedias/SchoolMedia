import datetime
from django.utils import timezone
import pytz
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from .models import User
# Create your views here.
tz = pytz.timezone('Asia/Shanghai')


@require_http_methods(["GET"])
def login(request):
    response = {}
    try:
        UserEmail = request.GET.get('Email')
        Userpassword = request.GET.get('password')
        print(UserEmail)
        print(Userpassword)
        user = User.objects.filter(Email=UserEmail).first()
        if user.Password == Userpassword:
            request.session['is_login'] = True
            request.session['UserID'] = user.User_ID
            response['is_login'] = True
            response['UserID'] = user.User_ID

    except:
        response['is_login'] = False

    return JsonResponse(response)



@require_http_methods(["POST"])
def Register(request):
    #RegiForm=RegisterForm()
    response = {}
    try:
        md1=User()
        md1.NickName=request.POST.get('NickName')
        print(md1.NickName)
        md1.Password=request.POST.get('Password')
        md1.Email=request.POST.get('Email')
        md1.Phone_number=request.POST.get('Phone_number')
        md1.Profile_photo=request.FILES.get('Profile_photo')
        print(request.FILES.get('Profile_photo'))
        md1.Background_photo=request.FILES.get('Profile_photo')
        print(timezone.now().astimezone(tz=tz).strftime("%Y-%m-%d %H:%M:%S"))
        now_time = timezone.now().astimezone(tz=tz).strftime("%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
        md1.Register_time=now
        if User.objects.filter(Email=md1.Email).first() is not None:
            print("Username has existed")
            print(User.objects.filter(Email=md1.Email))
            #print(NewStu)
        else:
            md1.save()
            print('success save')
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
        print(213)

    return JsonResponse(response)






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

