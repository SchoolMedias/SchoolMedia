from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


from .models import Liveroom,ManagerbUandL,ProhibitbUandL
from .serializers import LiveroomSerializer,ManagerbUandLSerializer,ProhibitbUandLSerializer

@api_view(["GET","POST"])
def rooms(request):
    if request.method == "GET":
        tdata = LiveroomSerializer(instance=Liveroom.objects.all(),many=True)
        return Response(data=tdata.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        tdata = LiveroomSerializer(data=request.data,partial=True)
        if tdata.is_valid():
            tdata.save()
            return Response(data=tdata.data,status=status.HTTP_201_CREATED)
        return Response(tdata.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
def room(request,roomid):
    try:
        troom = Liveroom.objects.get(roomID=roomid)
    except Liveroom.DoesNotExist:
        return Response(data={'data':'没有此直播间信息'},status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        tdata = LiveroomSerializer(instance=troom)
        return Response(data=tdata.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        tdata = LiveroomSerializer(instance=troom,data=request.data)
        if tdata.is_valid():
            tdata.save()
            return Response(data=tdata.data,status=status.HTTP_201_CREATED)
        return Response(tdata.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        troom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(["GET"])
def managers(request,roomid):
    try:
        Liveroom.objects.get(roomID=roomid)
    except Liveroom.DoesNotExist:
        return Response(data={'msg':'没有此直播间信息'},status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        tdata = ManagerbUandLSerializer(instance=ManagerbUandL.objects.filter(FLiveroom=roomid),many=True)
        return Response(data=tdata.data,status=status.HTTP_200_OK)
    
    
@api_view(["POST"])
def addmanager(request):
    if request.method == "POST":
        tdata = ManagerbUandLSerializer(data=request.data,partial=True)
        if tdata.is_valid():
            try:
                Liveroom.objects.get(roomID=request.data.get("FLiveroom"))
            except Liveroom.DoesNotExist:
                return Response(data={'msg':'没有此直播间信息'},status=status.HTTP_404_NOT_FOUND)
            if request.data.get("FUser") == Liveroom.objects.get(roomID=request.data.get("FLiveroom")).Owner:
                return Response(data={'msg':'人员冲突'},status=status.HTTP_409_CONFLICT)
            if ManagerbUandL.objects.filter(Q(FLiveroom=request.data.get("FLiveroom")) & Q(FUser=request.data.get("FUser"))):
                return Response(data={'msg':'已存在该房管信息'},status=status.HTTP_409_CONFLICT)
            tdata.save()
            return Response(data=tdata.data,status=status.HTTP_201_CREATED)
        return Response(tdata.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","DELETE"])
def manager(request,mid):
    try:
        tmanager = ManagerbUandL.objects.get(MID=mid)
    except ManagerbUandL.DoesNotExist:
        return Response(data={'msg':'没有此房管信息'},status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        tdata = ManagerbUandLSerializer(instance=tmanager)
        return Response(data=tdata.data,status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        tmanager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(["GET"])
def prohibits(request,roomid):
    try:
        Liveroom.objects.get(roomID=roomid)
    except Liveroom.DoesNotExist:
        return Response(data={'msg':'没有此直播间信息'},status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        tdata = ProhibitbUandLSerializer(instance=ProhibitbUandL.objects.filter(FLiveroom=roomid),many=True)
        return Response(data=tdata.data,status=status.HTTP_200_OK)
    
@api_view(["POST"])
def addprohibit(request):
    if request.method == "POST":
        tdata = ProhibitbUandLSerializer(data=request.data)
        if tdata.is_valid():
            try:
                print(request.data.get("FUser"))
                troom = Liveroom.objects.get(roomID=request.data.get("FLiveroom"))
            except Liveroom.DoesNotExist:
                return Response(data={'msg':'没有此直播间信息'},status=status.HTTP_404_NOT_FOUND)
            if request.data.get("FUser") == troom.Owner.User_ID:
                return Response(data={'msg':'人员冲突'},status=status.HTTP_409_CONFLICT)
            if ProhibitbUandL.objects.filter(Q(FLiveroom=request.data.get("FLiveroom")) & Q(FUser=request.data.get("FUser"))):
                return Response(data={'msg':'已存在该禁言信息'},status=status.HTTP_409_CONFLICT)
            tdata.save()
            return Response(data=tdata.data,status=status.HTTP_201_CREATED)
        return Response(tdata.errors,status=status.HTTP_400_BAD_REQUEST)    

@api_view(["GET","DELETE"])
def prohibit(request,pid):
    try:
        tmanager = ProhibitbUandL.objects.get(PID=pid)
    except ProhibitbUandL.DoesNotExist:
        return Response(data={'msg':'没有此禁言信息'},status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        tdata = ProhibitbUandLSerializer(instance=tmanager)
        return Response(data=tdata.data,status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        tmanager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    