import cv2
img = cv2.imread("0091.png")
crop_img = img[y:1920+200, x:1080+500]
cv2.imshow("x", crop_img)
cv2.waitKey(0)