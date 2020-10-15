from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class Faces(models.Model):
    """人脸库"""
    STATUS_CHOICES = (
        (u'E', u'生效'),
        (u'F', u'失效'),
    )
    name = models.CharField(u'名称', max_length=100)
    as_name = models.CharField(u'别名', max_length=100, blank=True, null=True)
    status = models.CharField(u'状态', choices=STATUS_CHOICES, max_length=10, blank=True, default='E')
    create_dt = models.DateTimeField(u'系统收录时间', default=timezone.now, blank=True,null= True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人脸库'
        verbose_name_plural = verbose_name

class FaceDetails(models.Model):
    """人脸库"""
    main = models.ForeignKey(Faces, verbose_name='人物', related_name='faces_main', on_delete=models.SET_NULL,
                             null=True, blank=True)

    file_name = models.CharField(u'文件名', max_length=100)
    folder = models.CharField(u'文件夹', max_length=100,null=True)
    #face_id = models.CharField(u'人脸库主键', max_length=50)

    create_dt = models.DateTimeField(u'系统收录时间', default=timezone.now, blank=True,null= True)

    def __unicode__(self):
        return self.file_name

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = '人脸详细信息'
        verbose_name_plural = verbose_name

class FaceCheckTemp(models.Model):
    """人脸待审核临时存放库"""

    name = models.CharField(u'姓名', max_length=100)
    username = models.CharField(u'上传用户', max_length=100)
    STATUS_CHOICES = (
        (u'S', u'通过'),
        (u'F', u'拒绝'),
        (u'D', u'待审核'),
    )
    status = models.CharField(u'状态', choices=STATUS_CHOICES, max_length=10, blank=True, default='D')
    img = models.FileField(u'上传文件', upload_to='static/upload_temp')
    create_dt = models.DateTimeField(u'系统收录时间', default=timezone.now, blank=True,null= True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人脸审核管理'
        verbose_name_plural = verbose_name
#上传文件
class UploadFileTemp(models.Model):
    img = models.FileField(u'上传文件',upload_to='static/upload_temp')
    create_dt = models.DateTimeField(u'系统收录时间', default=timezone.now, blank=True, null=True)

    def __unicode__(self):
        return self.img

    def __str__(self):
        return self.img
    class Meta:
        verbose_name = '临时上传文件'
        verbose_name_plural = verbose_name