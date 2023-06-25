from django.db import models


# Create your models here.
class videoClass(models.Model):
    class_ID = models.AutoField(primary_key=True, verbose_name="分区号")
    class_Name = models.CharField(max_length=255, verbose_name="分区名称")

    def __str__(self):
        return self.class_Name

    class Meta:
        db_table = "视频分区表"


class videoTable(models.Model):
    vid_ID = models.AutoField(primary_key=True, verbose_name="视频号")
    vid_Name = models.CharField(null=False, verbose_name="视频名称")
    vid_Time = models.CharField(max_length=255, verbose_name="视频投稿时间")  # 时间在函数中处理成字符串传入
    vid_PlayNum = models.IntegerField(default=0, verbose_name="视频播放量")
    vid_Class = models.ForeignKey(videoClass, on_delete=models.CASCADE, verbose_name="视频分区")  # 外键约束视频分区
    vid_File = models.FileField(upload_to="video/", verbose_name="视频文件")
    vid_CoverFile = models.ImageField(upload_to="video/", verbose_name="视频封面")

    def __str__(self):
        return self.vid_Name

    class Meta:
        db_Table = "视频表"


class videoContribute(models.Model):
    User = models.CharField(verbose_name="用户")  # 此处需要外键约束于用户表
    video = models.ForeignKey(videoTable, verbose_name="视频")

    def __str__(self):
        return self.User + "投稿了" + self.video

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["User", "video"], name="投稿唯一性约束")
        ]
        db_table = "视频投稿表"


class videoCompilations(models.Model):
    comp_ID = models.AutoField(primary_key=True, verbose_name="视频合集号")
    comp_Name = models.CharField(max_length=255, verbose_name="视频合集名称")
    video = models.ForeignKey(videoTable, verbose_name="视频")

    def __str__(self):
        return self.vidcomp_Name

    class Meta:
        db_table = "视频合集表"


class videoBulletComment(models.Model):
    bul_ID = models.AutoField(primary_key=True, verbose_name="视频弹幕号")
    bul_Comment = models.CharField(max_length=63, verbose_name="视频弹幕内容")
    bul_PlayTime = models.CharField(max_length=255, verbose_name="视频弹幕播放时间")  # 时间在函数中处理成字符串传入

    def __str__(self):
        return self.bul_Comment[:10]

    class Meta:
        db_table = "视频弹幕表"


class videoBulletCommentPush(models.Model):
    User = models.CharField(verbose_name="用户")  # 此处需要外键约束于用户表
    video = models.ForeignKey(videoTable, verbose_name="视频")
    bulletcomment = models.ForeignKey(videoBulletComment, verbose_name="弹幕")

    def __str__(self):
        return self.User + "在" + self.video + "发送了" + self.bulletcomment

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["User", "video", "bulletcommet"], name="弹幕唯一性约束")
        ]
        db_table = "视频弹幕发送表"



class videoLikeFavorite(models.Model):
    type_choices = (("like", "点赞"), ("favorite", "收藏"))

    LF_id = models.AutoField(primary_key=True, verbose_name="视频点赞收藏编号")
    User = models.CharField(verbose_name="用户")  # 此处需要外键约束于用户表
    Type = models.CharField(choices=type_choices, max_length=255, verbose_name="视频点赞收藏类型")
    video = models.ForeignKey(videoTable, verbose_name="视频")

    def __str__(self):
        return self.User + self.type_choices + self.video

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["User", "Type", "video"], name="点赞收藏唯一性约束")
        ]
        db_table = "视频点赞收藏表"


class videoComment(models.Model):
    com_ID = models.AutoField(primary_key=True, verbose_name="视频评论编号")
    comment = models.CharField(max_length=1023, verbose_name="视频评论")
    com_Time = models.CharField(max_length=255, verbose_name="视频评论时间")  # 时间在函数中处理成字符串传入

    def __str__(self):
        return self.comment

    class Meta:
        db_table = "视频评论表"


class videoCommentPush(models.Model):
    User = models.CharField(verbose_name="用户")  # 此处需要外键约束于用户表
    video = models.ForeignKey(videoTable, verbose_name="视频")
    comment = models.ForeignKey(videoComment, verbose_name="评论")

    def __str__(self):
        return self.User + "在" + self.video + "评论了" + self.comment

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["User", "video", "commet"], name="评论唯一性约束")
        ]
        db_table = "视频评论发送表"
