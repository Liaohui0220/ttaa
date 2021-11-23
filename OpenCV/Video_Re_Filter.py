# -*- coding: UTF-8 -*-
import cv2, shutil, os
from package import Path_list


def Filter(HW):
    files = Path_list.path_mp4(HW[2])
    f_h = HW[0].split('|')[0]
    f_w = HW[0].split('|')[1]

    ms = []
    for file in files:
        print(file)
        videoA = cv2.VideoCapture(file)
        get_w = str(videoA.get(cv2.CAP_PROP_FRAME_WIDTH)).split('.')[0]
        get_h = str(videoA.get(cv2.CAP_PROP_FRAME_HEIGHT)).split('.')[0]
        if HW[1] == '1':
            if f_h >= get_h and f_w >= get_w:
                ms.append(file)
        elif HW[1] == '2':
            if f_h <= get_h and f_w <= get_w:
                ms.append(file)
        else:
            print('输入有误！')
    for a in ms:
        try:
            b = a.replace(HW[2], HW[3])
            if not os.path.exists(b.rsplit('\\', 1)[0]):
                os.makedirs(b.rsplit('\\', 1)[0])

            shutil.move(a, b)
        except:
            print('移动出错！')


if __name__ == '__main__':
    print('用于过滤视频分辨率脚本,对于符合要求的mp4将会移动 20211014 v1')
    HW = []
    # HW.append(input('请输入分辨率分界线（帧高度|帧宽度）：'))
    # HW.append(input('请输入判断规则（1:大于等于|2：小于等于）：'))
    # HW.append(input('请输入需要处理的文件路径：'))
    # HW.append(input('请输入符合条件文件存放路径：'))

    HW.append('1080|1920')
    HW.append('2')
    HW.append(r'\\QMQ9982-1552\Users\qmq9982\Desktop\各比例视频\1280x720\540X960')
    HW.append(r'G:\测试\测试数据\Videos')

    Filter(HW)

    input('结束···')
