import subprocess
import time

ffmpeger = subprocess.Popen(
    'ffmpeg -ss 00:03:00 -i C:\Users\lh9373\Desktop\测试\测试数据\Video_Rect_DA\1\1.avi -to 00:02:00 -c copy C:\Users\lh9373\Desktop\测试\测试数据\Video_Rect_DA\1\2.avi',
    shell=True, stdin=subprocess.PIPE)


# ffmpeg -i C:\Users\lh9373\Desktop\测试\测试数据\Video_Rect_DA\2\1.avi -vf "select=between(n\,20\,200)" -y -acodec copy C:\Users\lh9373\Desktop\测试\测试数据\Video_Rect_DA\2\2.avi


time.sleep(2)
ffmpeger.stdin.write('q'.encode("GBK"))
ffmpeger.communicate()
