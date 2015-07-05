#!/usr/bin/env python
# coding:utf-8

import cv2
import numpy as np

def main():

    # カーネルの定義
    kernel = np.array([[0,-1,0],
                       [-1,5,-1],
                       [0,-1,0] ],np.float32)
    # カメラ映像の取得
    cap = cv2.VideoCapture("test.mov")

    while True:
        ret, im = cap.read()
        # 複数色チャンネルの分割
        if ret:
            b,g,r = cv2.split(im)
            # imと同じサイズの画像オブジェクト生成
            im2 =np.zeros((im.shape[0],im.shape[1],im.shape[2]),np.uint8)
            # im2は元画像の青→赤、緑→青、赤→緑
            im2[:,:,0] = r
            im2[:,:,1] = g
            im2[:,:,2] = b
            cv2.imshow("Camera",im)
            cv2.imshow(
            "Reverse",im2)
            # キーが押されたらループから抜ける
        else:
            print("damepo")

        if cv2.waitKey(10) > 0:
                break

    # キャプチャー解放
    cap.release()
    # ウィンドウ破棄
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()