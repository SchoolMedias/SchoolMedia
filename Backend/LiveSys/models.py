from django.db import models

# Create your models here.
class Liveroom(models.Model):
    roomID = models.AutoField(primary_key=True,verbose_name="roomID")
    roomName = models.CharField(max_length=100,verbose_name="roomName")
    roomInfo = models.CharField(max_length=2048,verbose_name="roomInfo")
    # Owner = models.ForeignKey(on_delete=models.CASCADE,verbose_name="Owner")

    class Meta:
        db_table = "直播间表"


class RelationbUandL(models.Model):
    RID = models.AutoField(primary_key=True,verbose_name="RID")
    # FUser = models.ForeignKey(on_delete=models.CASCADE,verbose_name="FUser")
    FLiveroom = models.ForeignKey(Liveroom,on_delete=models.CASCADE,verbose_name="FLiveroom")
    isManager = models.BooleanField(default=False,verbose_name="isManager")
    isProhibited = models.BooleanField(default=False,verbose_name="isProhibited")

    class Meta:
        db_table = "用户与直播间关系表"