import cv2
import easygui
import numpy as np
import os
import shutil

# 皮肤检测
def pi(res):
    y_cr_cb = cv2.cvtColor(res, cv2.COLOR_BGR2YCR_CB)  # 转换至YCrCb空间:y代表亮度，Cr表示红色分量信息，Cb表示蓝色分量信息
    #因为一般的图像都是基于RGB空间的，在RGB空间里人脸的肤色受亮度影响相当大，所以很难分离出肤色
    #如果把RGB转为YCrCb空间的话，可以忽略亮度(Y)的影响，肤色会很好提取
    (y, cr, cb) = cv2.split(y_cr_cb)  # 拆分出Y,Cr,Cb值
    # cv2.imshow("ycrcb",y_cr_cb)
    cr1 = cv2.GaussianBlur(cr, (5, 5), 0)
    # cv2.imshow("gaussianblur",cr1)
    _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Oust处理
    # cv2.imshow("threshold",skin)
    res = cv2.bitwise_and(res, res, mask=skin)
    # cv2.imshow("and",res)
    kernel = np.ones((3, 3), np.uint8)  # 设置卷积核
    erosion = cv2.erode(res, kernel)  # 腐蚀操作
    res = cv2.dilate(erosion, kernel)  # 膨胀操作,以上两步其实也可以直接做一个开运算
    # cv2.imshow("morphologyEx",res)
    return res

choice = input("请输入命令(1代表对视频截取图片，2代表从截取后的图片中寻找手势)：")
if choice == '1':
    # 读取视频帧
    if os.path.exists('handImg1'):#用来存放原图的文件夹
        shutil.rmtree('handImg1')#递归删除handImg1文件夹
    os.mkdir('handImg1')         #删除以后再创建一个
    if os.path.exists('handImg2'):#用来存放第一步处理过的数据的文件夹
        shutil.rmtree('handImg2')
    os.mkdir('handImg2')
    if os.path.exists('handOut'):
        shutil.rmtree('handOut')
    os.mkdir('handOut')
    num = 0#判断获得了多少张图片
    total = 0#只是用来计个数，每5帧截取一张图片
    cap = cv2.VideoCapture('D:\\My_opencv_python\\videos\\030\\030_001_01.avi')
    while cap.isOpened():
        ret, frame = cap.read()#ret的值为true或者false,frame表示读入的图片
        if ret:
            total += 1
            if total %5 == 0:#隔5帧取一张图片
                cv2.imwrite('./handImg1/%d.png' % num, frame)
                frame = pi(frame)
                cv2.imwrite('./handImg2/%d.png' % num, frame)
                num += 1
                cv2.imshow('a', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

    d_list = []
    for i in range(0, num - 1):
        im1 = cv2.imread('./handImg2/%d.png' % i)
        im2 = cv2.imread('./handImg2/%d.png' % (i + 1))
        d = 0
        result = cv2.subtract(im1, im2)
        d_list.append(d)
    with open('./handImg2/d_list.txt', 'w') as fp:
        fp.write(str(d_list))

# 三帧差法
elif choice == '2':
    with open('./handImg2/d_list.txt', 'r') as fp:
        d_list = fp.read()
    d_list = d_list[1:-1].split(',')
    get_point = []
    for i in range(1, len(d_list)):
        imOut = cv2.imread('./handImg1/%d.png' % i)
        im_size = imOut.shape
        w = im_size[0]
        h = im_size[1]
        im1 = cv2.imread('./handImg2/%d.png' % (i - 1))
        im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
        im2 = cv2.imread('./handImg2/%d.png' % i)
        im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
        im3 = cv2.imread('./handImg2/%d.png' % (i + 1))
        im3 = cv2.cvtColor(im3, cv2.COLOR_BGR2GRAY)
        im12 = cv2.absdiff(im1, im2)
        _, thresh1 = cv2.threshold(im12, 40, 255, cv2.THRESH_BINARY)
        im23 = cv2.absdiff(im2, im3)
        _, thresh2 = cv2.threshold(im23, 40, 255, cv2.THRESH_BINARY)
        thresh1 = cv2.medianBlur(thresh1, 9)
        thresh2 = cv2.medianBlur(thresh2, 9)
        k = np.ones((33, 33), np.uint8)
        thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, k)
        thresh2 = cv2.morphologyEx(thresh2, cv2.MORPH_CLOSE, k)
        binary = cv2.bitwise_and(thresh1, thresh2)

        contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            rect = cv2.minAreaRect(contours[0])
            points = cv2.boxPoints(rect)
            im2 = cv2.drawContours(im2, [points.astype(int)], 0, (255, 255, 255), 2)
            get_point = points.astype(int)
            #获得四个点的坐标
            x_list = [get_point[0][0], get_point[1][0], get_point[2][0], get_point[3][0]]
            y_list = [get_point[0][1], get_point[1][1], get_point[2][1], get_point[3][1]]
            test_len = 30  #框的扩充像素
            if min(y_list) < test_len:
                min_y = 0
            else:
                min_y = min(y_list) - test_len
            if min(x_list) < test_len:
                min_x = 0
            else:
                min_x = min(x_list) - test_len
            if max(y_list) > h - test_len:
                max_y = h
            else:
                max_y = max(y_list) + test_len
            if max(x_list) > w - test_len:
                max_x = w
            else:
                max_x = max(x_list) + test_len
            # 框大小阈值
            test3 = (max(y_list) - min(y_list)) * (max(x_list) - min(x_list))
            im_save = imOut[min_y:max_y, min_x:max_x]
            if test3 > 300:
                im_save = cv2.resize(im_save,(300,300))
                cv2.imwrite('./handOut/%d.png' % i, im_save)
        cv2.imshow('a', im2)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break