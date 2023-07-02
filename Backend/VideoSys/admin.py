from django.contrib import admin
from VideoSys import models

# Register your models here.
admin.site.register(models.videoClass)
admin.site.register(models.videoTable)
admin.site.register(models.videoContribute)
admin.site.register(models.videoCompilations)
admin.site.register(models.videoBulletComment)
admin.site.register(models.videoBulletCommentPush)
admin.site.register(models.videoLikeFavorite)
admin.site.register(models.videoComment)
admin.site.register(models.videoCommentPush)