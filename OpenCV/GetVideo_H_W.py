# -*- coding: utf-8 -*-
import cv2, shutil
from package import Path_list


def Move(datas):
    for a in datas[-1]:
        shutil.move(a, a.replace(a, datas[3]))
        print('Move:', a)


def Copy(datas):
    for a in datas[-1]:
        shutil.copy(a, a.replace(a, datas[3]))
        print('Copy:', a)


def H_W(datas):
    paths = Path_list.path_mp4(datas[0])
    HW = str(datas[1]).split('-')
    FPS = str(datas[2]).split('-')

    get_list = []
    for path in paths:
        print(path)
        videoA = cv2.VideoCapture(path)

        V_w = str(videoA.get(cv2.CAP_PROP_FRAME_WIDTH)).split('.')[0]
        V_h = str(videoA.get(cv2.CAP_PROP_FRAME_HEIGHT)).split('.')[0]
        V_fps = str(videoA.get(cv2.CAP_PROP_FPS)).split('.')[0]
        if HW[0] == V_h and HW[1] == V_w:
            if int(FPS[0]) < int(V_fps) < int(FPS[1]):
                get_list.append(path)
    datas.append(get_list)
    Copy(datas)


if __name__ == '__main__':
    datas = []
    print('用于找出固定宽高与特定帧数范围MP4视频工具 2021.5.30 V2 不支持中文')
    datas.append(input('输入视频路径：'))  # 0
    datas.append(input('请输入需要获取的高宽，用-隔开（1080-1920）：'))  # 1
    datas.append(input('请输入需要获取的帧率范围，从小到大用-隔开（59-61）：'))  # 2
    datas.append(input('输入要复制到的路径：'))  # 3

    H_W(datas)

    input('结束···')
