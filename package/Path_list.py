#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


# 获取文件
def path_txt(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt') | file.endswith('.TXT'):
                path1.append(os.path.join(root, file))
    return path1


def path_avi(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.avi') | file.endswith('.AVI'):
                path1.append(os.path.join(root, file))
    return path1


def path_pnt(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.pnt') | file.endswith('.PNT'):
                path1.append(os.path.join(root, file))
    return path1


def path_jpg(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jpg') | file.endswith('.JPG') | file.endswith('.JPEG') | file.endswith('.jpeg'):
                path1.append(os.path.join(root, file))
    return path1


def path_mp4(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.mp4') | file.endswith('.MP4'):
                path1.append(os.path.join(root, file))
    return path1


def path_png(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.png') | file.endswith('.PNG'):
                path1.append(os.path.join(root, file))
    return path1


def path_raw(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.raw'):
                path1.append(os.path.join(root, file))
    return path1


def path_prop(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.prop') | file.endswith('.PROP'):
                path1.append(os.path.join(root, file))
    return path1


def path_json(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.json') | file.endswith('.JSON'):
                path1.append(os.path.join(root, file))
    return path1


def path_all(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            path1.append(os.path.join(root, file))
    return path1


def path_AllImg(path):
    path1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jpg') | file.endswith('.JPG') | file.endswith('.jpeg') | file.endswith('.JPEG') | file.endswith('.png') | file.endswith('.PNG') | file.endswith('.nv12') | file.endswith('.NV12'):
                path1.append(os.path.join(root, file))
    return path1

# 对列表按照windows时间排序
# def update_time_sequence(file_path):
#     dir_list = os.listdir(file_path)
#     if not dir_list:
#         return
#     else:
#         # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
#         # os.path.getmtime() 函数是获取文件最后修改时间
#         # os.path.getctime() 函数是获取文件最后创建时间
#         dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
#         return dir_list
#
#
# dir_list = sorted(path1_list, key=lambda x: os.path.getmtime(os.path.join(path_olds, x)))
