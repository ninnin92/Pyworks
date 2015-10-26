#!/usr/bin/env python
# coding:utf-8

import os
import cv2

# 最終的にグラフ描画までやること
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# フォルダの中身をすべてリストに
image_list = os.listdir("lena/")

# 分類器の設定
cascade_folder = "/Users/Furuhata/.pyenv/versions/miniconda3-3.16.0/pkgs/opencv3-3.0.0-nppy34_0/share/OpenCV/"
cascade_xml0 = "haarcascades/haarcascade_frontalface_default.xml"
cascade_xml1 = "haarcascades/haarcascade_frontalface_alt.xml"
cascade_xml2 = "haarcascades/haarcascade_frontalface_alt2.xml"
cascade_xml4 = "lbpcascades/lbpcascade_frontalface.xml"
cascade_path = cascade_folder + cascade_xml0
cascade = cv2.CascadeClassifier(cascade_path)

color = (255, 255, 255)  # 白
data = pd.DataFrame()
face_df = pd.DataFrame()
px_list = list(range(100, 650, 50))


for im in image_list:
    face_list = []
    image_path = "lena/" + im
    image = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
    print(image_path)
    print(facerect)

    if len(facerect) > 0:
        for (x, y, w, h) in facerect:
            face = pd.DataFrame({"x": [x], "y": [y],  "width": [w]})
            cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness=2)
            cv2.imwrite("output_normal/result_" + im + ".jpg", image)
            face_df = pd.concat([face_df, face])
    else:
        print("No face")
        face = pd.Series({"x": [0], "y": [0],  "width": [0]})
        face_df = pd.concat([face_df, face])

    max_ix = face_df["width"].argmax()  # 良くない：顔に対して二重に出ると防ぎようがない
    face_df = face_df.ix[max_ix]
    data = pd.concat([data, face_df])

else:
    print("detection finish!!!!")

print(data)
#sb.pointplot(x="px", y="width", data=data, markers=["o"], linestyles=["-"])
#sb.plt.show()

