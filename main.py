# coding=utf-8
# 图片修复
from cv2 import cv2
import numpy as np
import os

base_path = "/mnt/d/github/image-clear-text/5757/"
for img_file in os.listdir(base_path):
    path = base_path + img_file

    img = cv2.imread(path)
    # hight, width, depth = img.shape[0:50]

    # 图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
    thresh = cv2.inRange(img, np.array([0, 0, 0]), np.array([200, 200, 200]))

    # 创建形状和尺寸的结构元素
    kernel = np.ones((3, 3), np.uint8)
    # 扩张待修复区域
    hi_mask = cv2.dilate(thresh, kernel, iterations=5)
    specular = cv2.inpaint(img, hi_mask, 8, flags=cv2.INPAINT_TELEA)

    # cv2.namedWindow("Image", 0)
    # cv2.imshow("Image", img)
    # cv2.namedWindow("newImage", 0)
    # cv2.imshow("newImage", specular)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    new_img_path = base_path + img_file
    cv2.imwrite(new_img_path, specular, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
