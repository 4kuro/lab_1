import cv2
import numpy as np

#img = cv2.imread('pens.jpg')
#img2 = cv2.imread('pens.jpg')

#img = cv2.imread('low_res_img.jpg')
#img2 = cv2.imread('low_res_img.jpg')

#img = cv2.imread('notes.jpg')
#img2 = cv2.imread('notes.jpg')

#img = cv2.imread('text.jpg')
#img2 = cv2.imread('text.jpg')

img = cv2.imread('yellow.jpg')
img2 = cv2.imread('yellow.jpg')


if img is None:
    print("Не удалось загрузить изображение.")
else:
    (row, col) = img.shape[0:2]
    for i in range(row):    # Конвертування зображення в чб варіант
        for j in range(col):
            img[i, j] = sum(img[i, j]) * 0.3
    
    thresh = 128 # значення границі

    binary_img = np.zeros_like(img)
    for i in range(row):     # Глобальна бінарізація
        for j in range(col):
            if img[i, j][0] > thresh:
                binary_img[i, j] = 255
            else:
                binary_img[i, j] = 0

    color_result_img = np.zeros_like(img)

    for i in range(row):
        for j in range(col):
            if binary_img[i, j][0] == 255:  # Зміна білих пікселей на кольорові
                color_result_img[i, j] = img2[i, j]


    cv2.imshow('Cut-out image', color_result_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()