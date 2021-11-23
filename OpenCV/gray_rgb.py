# -*- coding: UTF-8 -*-
import cv2
from package import Path_list

# 将灰度图转换为rgb图，不支持中文路径


file_old = r'Z:\\'
file_save = r'Y:\\'

paths = Path_list.path_png(file_old)

b = 0
for a in paths:

    b += 1
    print(b, len(paths), '\n', a)
    try:
        img = cv2.imread(a)
        IMG_OUT = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite(a.replace(file_old, file_save), IMG_OUT, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    except:
        print('异常', a)