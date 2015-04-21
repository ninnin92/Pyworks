#!/usr/bin/env python
# coding:utf-8

# 参考サイト：http://python-gazo.blog.jp/opencv/%E9%A1%94%E8%AA%8D%E8%AD%98_Web%E3%82%AB%E3%83%A1%E3%83%A9

import os
import cv2
import numpy as np

if __name__ == '__main__':

    if not os.path.exists('output'):  #なければ作成
        os.mkdir('output')

    videos = "test.mov"
    # file_list = os.listdir("input/")  # フォルダの中の動画を全部分析する際に（フォルダ内にあるファイルのリストを返す）

    # Logの準備
    out_list = []
    fp = open('output/face_pos.csv', 'w')  # CSVファイルを開く（"w"は書き込みオプション）
    title = ['videos', 'frameN', 'pos_x', 'pos_y', 'width', 'height']  # ラベルの指定

    # ラベルだけ先に記入（絶対にもっとスマートな書き方があるはず）
    for t in title:
        fp.write('%s,' % t)
    fp.write('\n')  # 改行
    fp.flush()  # 一旦書き込み

    # グレースケール & サイズ削減 ver（軽い）

    # videos = "input/" + videos  # inputフォルダから拾うように

    # カメラ映像の取得
    cap = cv2.VideoCapture(videos)  # 0だとカメラを取得、ファイル名を記述

    # ビデオ出力準備
    w = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))  # 出力ビデオの幅
    h = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))  # 出力ビデオの高さ
    fourcc = cv2.cv.CV_FOURCC("m", "p", "4", "v")  # 出力ビデオのコーデック（現在は.mov用に）
    out = cv2.VideoWriter("output.mov", fourcc, 30, (w/2, h/2))  # 出力ビデオのセット

    # 顔探索用の機械学習ファイルを取得
    cascade = cv2.CascadeClassifier("/usr/local/Cellar/opencv/2.4.11/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml")

    frameN = 0  # frameカウント用に

    while(1):
        ret, im = cap.read()  # 1フレームずつ読み込み？
        if ret:  # 読み込まれている時のみ処理
            frameN = frameN + 1
            im = cv2.resize(im, (im.shape[1]/2, im.shape[0]/2))  # 動画サイズを半分に
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)
            # 顔探索(画像,縮小スケール,最低矩形数)
            face = cascade.detectMultiScale(gray, 1.1, 3)
            # 顔検出した部分を長方形で囲う
            for (x, y, w, h) in face:
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 50, 255), 3)
                out_list.append([videos] + [frameN] + [x] + [y] + [w] + [h])  # データのリストを作成

            # 画像表示（リアルタイム表示：重い）
            # cv2.imshow('Video Stream', gray)

            out.write(im)  # 動画の書き込み
        else:
            break

        # キーが押されたらループから抜ける
        if cv2.waitKey(10) > 0:
            cap.release()
            cv2.destroyAllWindows()
            break

    # Logの書き込み
    for r in out_list:
        fp.write('%s,%d,%d,%d,%d,%d\n' % tuple(r))  # 書き込む文字の型によって%の後のアルファベットを変える
    fp.write('\n')
    fp.write('\n')  # ２段空白を空ける
    fp.flush()

    # キャプチャー解放
    cap.release()
    # Video writerの解放（必須）
    out.release()
    # ウィンドウ破棄
    cv2.destroyAllWindows()
