from django.db import models
from UserSys import models as Umodels
# Create your models here.


class Meeting(models.Model):
    Meeting_id = models.AutoField(primary_key=True)
    Presenter = models.ForeignKey(Umodels.User, related_name='owner', on_delete=models.CASCADE)
    Start_time = models.DateTimeField()
    End_time = models.DateTimeField()
    Meeting_Status = models.IntegerField(choices=((0,'未开始'),(1,'进行中'),(2,'已结束')))

    def __str__(self):
        return self.Meeting_id + self.Presenter + "的会议"

    class Meta:
        db_table = "会议表"





class Blacklist(models.Model):
    Item_id = models.AutoField(primary_key=True)
    BanUser = models.ForeignKey(Umodels.User, on_delete=models.CASCADE)
    MeetingRoom = models.ForeignKey(Meeting, blank=True, default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.BanUser + "禁止加入" + self.Meeting

    class Meta:
        db_table = "黑名单表"



