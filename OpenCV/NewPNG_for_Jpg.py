import numpy as np, cv2
from package import Path_list
from PIL import Image

#
# def New_png(paths_file):
#     for file in paths_file:
#         print(file)
#         img_h = Image.open(file)
#         w = img_h.width
#         h = img_h.height
#
#         # 生产灰度图
#         img = np.zeros((h, w), dtype=np.uint8)
#         print(img)
#         # 转RGB
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         # 保存
#         cv2.imencode('.png', img)[1].tofile(str(file).replace('.jpg', '.png'))
#
#
# if __name__ == '__main__':
#     file_path = r'C:\Users\lh9373\Desktop\测试\测试数据\Image\哈士奇'
#     paths_file = Path_list.path_jpg(file_path)
#     New_png(paths_file)
#     input('结束···')
import cv2
import np

# a = np.matlib.eye(n=10, M=10, dtype=int)
# b = np.matlib.zeros((2, 2))

# 创建多维数组
list1 = [[[1] * 3 for _ in range(10)] for _ in range(10)]
list1 = np.asarray(list1)
cv2.imencode('.jpg', list1)[1].tofile(r'C:\Users\lh9373\Desktop\111\2.jpg')
print(list1)



file = cv2.imread(r'C:\Users\lh9373\Desktop\111\T1.png')
print(file)
cv2.imshow('tet', list1)
cv2.waitKey()
