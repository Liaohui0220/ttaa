import cv2

# 创建显示窗口
cv2.namedWindow('Video')

# # 导入视频文件，参数：0 自带摄像头，1 USB摄像头，为文件名时读取视频文件
# video_capture = cv2.VideoCapture(0)


path1 = r'C:\Users\lh9373\Desktop\测试\测试数据\Video_Rect_DA\n00002.mkv_20210325_095228.avi'
video_capture = cv2.VideoCapture(path1)

# 获取读入视频的参数
fps = video_capture.get(cv2.CAP_PROP_FPS)
width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('fps:', fps)
print('width:', width)
print('height:', height)

# 定义截取尺寸,后面定义的每帧的h和w要于此一致，否则视频无法播放
size = (int(3000), int(6000))  # (height, width)

# 创建视频写入对象
video_writer = cv2.VideoWriter("test.avi",
                               cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                               fps,
                               size)

# 读取视频帧，然后写入文件并在窗口显示
success, frame = video_capture.read()
while success and not cv2.waitKey(1) == 27:
    # 定义ROI的位置
    frame = frame[0:6000, 0:3000]  # [width, height] 要与上面定义的size参数一致，注意参数的位置
    video_writer.write(frame)  # 写入视频文件
    cv2.imshow("video", frame)
    success, frame = video_capture.read()

# 回收资源
cv2.destroyWindow("video")
video_capture.release()
