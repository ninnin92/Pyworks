# -*- coding: utf-8 -*-
import cv2

if __name__ == '__main__':
    # カメラ映像の取得
    cap = cv2.VideoCapture(0)
    # 目探索用の機械学習ファイルを取得
    cascade = cv2.CascadeClassifier("/usr/local/Cellar/opencv/2.4.11/share/OpenCV/haarcascades/haarcascade_eye.xml")
    # 画像の読み込み
    while(1):
        ret, im = cap.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # 色をグレーに
        gray = cv2.resize(gray, (gray.shape[1]/2, gray.shape[0]/2))  # 動画サイズを半分に
        # 目探索(画像,縮小スケール,最低矩形数)
        eye = cascade.detectMultiScale(gray, 1.1, 3)
        for (x, y, w, h) in eye:    # 目検出した部分を長方形で囲う
            print(eye)
            cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 50, 255), 3)

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