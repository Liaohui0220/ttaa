#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PIL import Image  # 如果没有该库，请 pip install PIL
import numpy  # 如果没有该库，请 pip install numpy

frame = 10  # 每秒10帧, 即一秒十张


def get_image(video_path, image_path):
    try:
        os.system(
            'F:/FFmpeg/ffmpeg-N-101711-ga4e518c321-win64-gpl-shared-vulkan/bin/ffmpeg -i  {0} -r {1} -f image2 {2}\%05d.png'.format(
                video_path, frame, image_path))
    except:
        print('ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


if __name__ == '__main__':
    get_image(r'C:\Users\lh9373\Desktop\测试\测试数据\Video_Rect_DA\1\1.avi', 'Results')