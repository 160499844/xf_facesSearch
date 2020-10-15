import face_recognition
import os
import numpy as np
import datetime
# Often instead of just checking if two faces match or not (True or False), it's helpful to see how similar they are.
# You can do that by using the face_distance function.

# The model was trained in a way that faces with a distance of 0.6 or less should be a match. But if you want to
# be more strict, you can look for a smaller face distance. For example, using a 0.55 cutoff would reduce false
# positive matches at the risk of more false negatives.

# Note: This isn't exactly the same as a "percent match". The scale isn't linear. But you can assume that images with a
# smaller distance are more similar to each other than ones with a larger distance.

basepath = "V:\\resource\\faceSearch\\faces_test\\"
baseSavePath = "V:\\resource\\faceSearch\\faces_file\\"
def loadFaceData(img_path):
    """返回人脸数据"""
    known_obama_image = face_recognition.load_image_file(img_path)
    d = face_recognition.face_encodings(known_obama_image)
    if len(d) == 0:
        return ""
    obama_face_encoding = d[0]
    return obama_face_encoding

def get_all_files(dir,lastName):
    """"获取所有图片文件"""
    files_ = []
    list_ = os.listdir(dir)
    for i in range(0, len(list_)):
        path = os.path.join(dir, list_[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path,lastName))
        if os.path.isfile(path):
            if path.endswith("." + lastName):
                files_.append(path)
    return files_
def getImgs():
    imgs = get_all_files(baseSavePath,"npy")
    return imgs

def loadFaces():
    """加载人脸数据"""
    #known_encodings = []# 已知人脸数据
    headers = getImgs()
    print("加载人脸数据")
    return headers

def searchFace(headers,image_to_test_encoding,top):
    result = {}
    facesDatas = []
    names = []
    for header in headers:
        #print(header)
        # name = str(header).replace(basepath,"")
        # name = name.split("\\")[0]
        # name_path = baseSavePath + name
        # if os.path.isfile(name_path + '.npy'):
        #     faceData = np.load(name_path + '.npy')
        # else:
        #     faceData = loadFaceData(header)
        #     np.save(name_path, faceData)
        faceData = np.load(header)
       # print(faceData)
        known_encodings = []  # 已知人脸数据
        known_encodings.append(faceData)
        names.append(header)
        facesDatas.append(known_encodings)
        # See how far apart the test image is from the known faces
    j = -1 
    start = datetime.datetime.now()
    for item in facesDatas:
        j += 1
        try:
            face_distances = face_recognition.face_distance(item, image_to_test_encoding)

            for i, face_distance in enumerate(face_distances):

                if face_distance < 0.5:
                    sp = ""
                    if '\\' in names[j]:
                        sp = "\\"
                    if '/' in names[j]:
                        sp = "/"
                    n = str(names[j]).split(sp)[-1].replace(".npy","")
                    result[n] = round(face_distance,2)


        except Exception as e:
            print(names[j] + "-出错")
            print(e)
            if os.path.isfile(names[j]):
                pass
                #os.remove(names[j])
    end = datetime.datetime.now()
    print("人脸匹配耗时:%s" % (end - start))

    start = datetime.datetime.now()
    d_order = sorted(result.items(), key=lambda x: x[1], reverse=False)[:top]  # 按字典集合中，每一个元组的第二个元素排列。
    for item in d_order:
        print(item)
    end = datetime.datetime.now()
    print("排序耗时:%s" % (end - start))
    return d_order
if __name__ == '__main__':
    start = datetime.datetime.now()
    faces=loadFaces()
    # 需要判断的人脸
    image_to_test_encoding = loadFaceData("V:\\resource\\faceSearch\\main.jpg")
    searchFace(faces,image_to_test_encoding,1)
    end = datetime.datetime.now()
    print("程序运行耗时:%s" %(end - start))

    # x = np.arange(10)
    # np.save(baseSavePath + 'save_x', x)