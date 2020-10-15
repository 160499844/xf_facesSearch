from django.apps import AppConfig


import application.faces.checkFace as facesUtils
import datetime
class DatabasecenterConfig(AppConfig):
    name = 'databaseCenter'

facesData = []

def initFaceData():
    print("初始化人脸数据")
    global facesData
    facesData = facesUtils.loadFaces()
    print("初始化完毕")

def getFacesData():
    return facesData

def searchFaces(img,top):
    faces = getFacesData()
    # 需要判断的人脸
    image_to_test_encoding = facesUtils.loadFaceData(img)
    return facesUtils.searchFace(faces, image_to_test_encoding,top)
