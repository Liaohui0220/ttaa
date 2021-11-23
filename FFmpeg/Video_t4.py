import os


# 过滤坏帧
def FFm_video(cmd_list):
    #  获取关键帧（I帧）的位置 应用FFmpeg解决
    cmd = r'ffprobe -i ' + cmd_list[0] + ' -select_streams v -show_frames -show_entries frame=pict_type'
    res = os.popen(cmd)  # 调起CMD
    output_str = res.read()  # 获得输出字符串
    print(res.read())
    output_str = str(output_str).replace('[/FRAME]\n', '').replace('[FRAME]\n', '').split('\n')
    a = 0
    while a < len(output_str):
        if output_str[a] == 'pict_type=I':
            print(a)
            break
        a += 1
    return a


if __name__ == '__main__':
    FFm_video([r'C:\Users\lh9373\Desktop\testvide\1.mp4'])
