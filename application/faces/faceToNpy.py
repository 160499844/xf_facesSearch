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

basepath = "V:\\resource\\faceSearch\\faces\\"
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
    imgs = get_all_files(basepath,"jpg")
    return imgs

def loadFaces():
    """对人脸进行缓存"""
    #known_encodings = []# 已知人脸数据
    headers = getImgs()
    for header in headers:
        #print(header)
        name = str(header).replace(basepath,"")
        name = name.split("\\")[0]
        name_path = baseSavePath + name
        if os.path.isfile(name_path + '.npy'):
            continue
        # if os.path.isfile(name_path + '.npy'):
        #     faceData = np.load(name_path + '.npy')
        # else:
        try:
            faceData = loadFaceData(header)
            np.save(name_path, faceData)
            print(name)
        except:
            print(name+"错误")



if __name__ == '__main__':
    start = datetime.datetime.now()
    loadFaces()

    end = datetime.datetime.now()
    print("程序运行耗时:%s" %(end - start))

    # x = np.arange(10)
    # np.save(baseSavePath + 'save_x', x)