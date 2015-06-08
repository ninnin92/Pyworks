#!/usr/bin/env python
# coding:utf-8

# 参考：http://python-gazo.blog.jp/opencv/%E9%A1%94%E8%AA%8D%E8%AD%98_Web%E3%82%AB%E3%83%A1%E3%83%A9

import cv2
import numpy as np

# グレースケール & サイズ削減 ver（軽い）
if __name__ == '__main__':

    # カメラ映像の取得
    cap = cv2.VideoCapture(0)  # 0だとカメラを拾う、ファイル名を記述することも可
    # 顔探索用の機械学習ファイルを取得（検出器）
    cascade = cv2.CascadeClassifier("/usr/local/Cellar/opencv/2.4.11/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml")  # haarcascade_frontalface_alt.xml
    cascade_eye = cv2.CascadeClassifier("/usr/local/Cellar/opencv/2.4.11/share/OpenCV/haarcascades/haarcascade_eye.xml")

    while(1):
        ret, im = cap.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # 色をグレーに
        gray = cv2.resize(gray, (gray.shape[1]/2, gray.shape[0]/2))  # 動画サイズを半分に
        # 顔探索(画像,縮小スケール,最低矩形数)
        face = cascade.detectMultiScale(gray, 1.1, 3)
        for (x, y, w, h) in face:
            face_ROI = gray[y:y+h, x:x+w]  # ROIの設定
            eye = cascade_eye.detectMultiScale(face_ROI, 1.1, 3)  # 目の探索
            if not len(eye) == 0:
                print("eye detect")
                # 顔検出した部分を長方形で囲う
                cv2.rectangle(gray, (x, y), (x+w, y+h), 255, 3)
                print(face)  # 顔座標の表示
            else:
                pass

        # 画像表示
        cv2.imshow("Show Image", gray)
        # キーが押されたらループから抜ける
        if cv2.waitKey(10) > 0:
            cap.release()
            cv2.destroyAllWindows()
            break

    # キャプチャー解放
    cap.release()
    # ウィンドウ破棄
    cv2.destroyAllWindows()

# カラー & 通常サイズ ver（激重）
"""

if __name__ == '__main__':

    # カメラ映像の取得
    cap = cv2.VideoCapture(0)
    # 顔探索用の機械学習ファイルを取得
    cascade = cv2.CascadeClassifier("/usr/local/Cellar/opencv/2.4.11/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml")
    while(1):
        ret, im = cap.read()
        # 顔探索(画像,縮小スケール,最低矩形数)
        face = cascade.detectMultiScale(im, 1.1, 2)

        print(face)　# 顔座標の表示

        # 顔検出した部分を長方形で囲う
        for (x, y, w, h) in face:
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 50, 255), 3)

        # 画像表示
        cv2.imshow("Show Image", im)
        # キーが押されたらループから抜ける
        if cv2.waitKey(10) > 0:
            cap.release()
            cv2.destroyAllWindows()
            break

    # キャプチャー解放
    cap.release()
    # ウィンドウ破棄
    cv2.destroyAllWindows()"""
