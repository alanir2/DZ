import cv2
import numpy as np

img = cv2.imread('imagn/color_text.jpg')
print(img.shape)

new_img = np.zeros(img.shape, dtype='uint8')
# cv2.imshow('result', img)
#
# cv2.waitKey(0) # Для запуска картинки 0 это бесконечность, 10000 это 1 сек.

# cap = cv2.VideoCapture('vidio/1.webm')
#
# while True:
#     success, img =cap.read()
#     cv2.imshow('result', img)
#
#     if  cv2.waitKey(1)&0xFF == ord('q'):# waitKey(1) время ожидания 1 = 1 сек.
#         break

# print(img.shape) # размеры картинки первый элемент отвечает за высоту

# new_img = cv2.resize(img, (700, 300)) # изменение размера кртинки
# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) # уменьшене картинки ровно в два раза
# cv2.imshow('result', new_img)


img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # меняет цвет на серый
img = cv2.GaussianBlur(img, (9, 9), 0)# размытие, числа должны быть не четные

img = cv2.Canny(img, 20, 30) # переводит в черно белый формат(чем меньше число, тем выше точность)
#
kernel = np.ones((3, 3), np.uint8)
img= cv2.dilate(img, kernel, iterations=1) # увеличивает жирность обводки

img = cv2.erode(img, kernel, iterations=1)

# img= cv2.flip(img, 0) # отражерие картинки

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# print(con, hir) #выводит количество точек
# sel_countours=[]
# for i in range(377):
#     sel_countours.append(con[i])
# cv2.drawContours(new_img, sel_countours, -1, (250,125,200),2)


cv2.drawContours(new_img, con[85: 160], -1, (250, 125, 200), 2)
cv2.drawContours(new_img, con[0: 85], -1, (230, 111, 48), 2)
cv2.drawContours(new_img, con[170: 377], -1, (75, 184, 39), 2)

cv2.imshow('result', new_img)

cv2.waitKey(0)
