from rest_framework.response import Response
from rest_framework import status
#  判断是否登录装饰器
def islogin(func):
    def inner(request, *args, **kwargs):
        tuserid = request.session.get("userid",None)
        if not tuserid:
            return Response(data={'msg':'未登录'},status=status.HTTP_400_BAD_REQUEST)
        print(tuserid)
        return func(request, *args, **kwargs)
    return inner