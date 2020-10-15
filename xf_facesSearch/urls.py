"""xf_facesSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import app.views as d_views
import app.apps as apps

#初始化人脸数据
apps.initFaceData()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('face/search/', d_views.searchFace),  # 人脸搜索
    path('face/upload/', d_views.uploadFace),  # s上传人脸
    path('faces/agree/', d_views.agreeFace),  # 审核通过人脸
   # path('faces/unAgree/', d_views.unAgreeFace),  # 拒绝人脸
]
