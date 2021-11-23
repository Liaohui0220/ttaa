import cv2

videoCapture = cv2.VideoCapture(r'C:\Users\lh9373\Desktop\测试\测试数据\Video_Rect_DA\n00002.mkv_20210325_095228.avi')
video_size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
video_fps = int(videoCapture.get(5))
fps = video_fps  # 保存视频的帧率
size = video_size  # 保存视频的大小

videoWriter = cv2.VideoWriter('video4.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)
i = 0

while True:
    success, frame = videoCapture.read()
    if success:
        i += 1
        if (i >= 20 and i <= 100):
            videoWriter.write(frame)
    else:
        print('end')
        break

# video_path = r"C:\Users\lh9373\Desktop\测试\测试数据\Video_Rect_DA\n00002.mkv_20210325_095228.avi"
# video_capture = cv2.VideoCapture(video_path)
#
# video_size = (int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
#               int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# print("video size:{}".format(video_size))  # (540, 960)
# 视频总帧数
# total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))  # 799
# print("total_frame:{}".format(total_frames))

# 视频帧率
# video_fps = int(video_capture.get(5))
# print("video_fps:{}".format(video_fps))
# print("video_fps_1:{}".format(video_fps_1))
# video_FourCC = int(video_capture.get(cv2.CAP_PROP_FOURCC))  # 视频编码
# video_width = int(video_capture.get(3))
# video_height = int(video_capture.get(4))
