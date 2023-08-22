from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .auth import islogin

@api_view(["POST"])
def login(request):
    if request.method == 'POST':  
        request_json = request.data
        email = request_json.get("Email")
        password = request_json.get("Password")
        if not email or not password:
            return Response(data={'msg':'不合理信息'},status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.filter(Email=email).first()
            if not user:
                return Response(data={"msg": "不存在该用户"}, status=status.HTTP_404_NOT_FOUND)
            else:
                if password == user.Password:
                    request.session["userid"] = user.User_ID
                    return Response(data={"msg": "登录成功"}, status=status.HTTP_200_OK)
                else:
                    return Response(data={"msg": "密码错误"}, status=status.HTTP_403_FORBIDDEN)

        