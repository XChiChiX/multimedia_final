import cv2
import numpy as np
from matplotlib import pyplot as plt

def imgBinQuan(img):
    # 獲取影像的高度和寬度
    nr,nc = img.shape[:2]
    # 建立一幅影像，內容使用零填充
    new_img = np.zeros((nr, nc, 3), np.uint8)
    for i in range(nr):
        for j in range(nc):
            for k in range(3):  # 對應RGB三通道                
                if img[i, j][k] < 128:
                    gray = 0
                else:
                    gray = 255
                new_img[i, j][k] = np.uint8(gray)                 
    return new_img 

# def image_merge(img1, img2):
#     img1 = cv2.resize(img1, (1000, 500))
#     img2 = cv2.resize(img2, (1000, 500))
#     # print(img2.shape)

#     result = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
#     return result

def start(img1_name, img2_name):
    img1 = cv2.imread(img1_name)
    img2 = cv2.imread(img2_name)

    img1 = cv2.resize(img1, (1000, 500))
    img2 = cv2.resize(img2, (1000, 500))

    img1 = imgBinQuan(img1[:,:,::-1])
    img2 = imgBinQuan(img2[:,:,::-1])

    dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

    # plt.imshow(dst)
    # plt.show()

    cv2.imwrite('merge.png', dst)