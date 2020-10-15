from django.shortcuts import render
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import os
import json
import app.apps as apps
from app.models import *

# Create your views here.
@csrf_exempt
def searchFace(request):
  img = request.FILES.get('file')
  upload = UploadFileTemp()
  list = []
  upload.img = img
  upload.save()
  print(upload.img.url)
  cwd = os.getcwd()
  path = cwd + '/' + upload.img.url
  message = {'message': '上传成功', 'url': path}
  result = apps.searchFaces(path,10)
  names = []
  facesDetails = []
  if len(result) == 0:
    message = {'message': "暂无数据", 'code': -1}
    return HttpResponse(json.dumps(message), content_type="application/json")
  for item in result:
    #print("item=" + "".join(item))
    #names.append("'"+item[0]+"'")
    #sql = "select * from databaseCenter_facedetails where folder = '%s' " %item[0]
    try:
      facesDetailsQuery = FaceDetails.objects.get(folder=item[0])
      facesDetails.append(facesDetailsQuery)
    except:
      print("%s查询失败" %item[0])
  #sql = "select * from databaseCenter_facedetails where folder in (%s)" %(",".join(names))
    #print(sql)
  #facesDetails = FaceDetails.objects.raw(sql)
  for item in facesDetails:

    url = item.folder + "/" + item.file_name
    D_item = {
      "name" : item.folder,
      "url" :url,
    }
    print(D_item)
    list.append(D_item)
  message = {'message': list,'code':0}
  return HttpResponse(json.dumps(message), content_type="application/json")

@csrf_exempt
def uploadFace(request):
  try:
    img = request.FILES.get('file')
    name = request.POST['name']
    #upload = UploadFileTemp()
    list = []
    #upload.img = img
    #upload.save()
    lastName = str(img.name).endswith(".jpg")
    if lastName == False:
      message = {'message': '仅支持jpg格式后缀名!'}
    else:
      faceTemp = FaceCheckTemp()
      faceTemp.img = img
      faceTemp.username = 'test'
      faceTemp.name = name
      faceTemp.save()

      message = {'message': '请求已经提交，请等待审核!'}
  except:
    message = {'message': '提交失败'}

  return HttpResponse(json.dumps(message), content_type="application/json")


def agreeFace(request):
  try:
    id = request.GET['id']
    facesTemp = FaceCheckTemp.objects.get(id=id)
    facesTemp.status = 'S'
    facesTemp.save()
    face = Faces.objects.filter(name=facesTemp.name).filter()
    faces = FaceDetails.objects.filter(main=face)
    for item in faces:
      item.delete()
    face.delete()
    newFace = Faces()
    newFace.name = facesTemp.name
    newFace.save()
    newFacesDetails = FaceDetails()
    newFacesDetails.main = newFace

    newFacesDetails.save()
  except:
    pass