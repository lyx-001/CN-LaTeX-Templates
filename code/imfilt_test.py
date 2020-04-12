from cv2 import cv2
img = cv2.imread('./image/cat.jpg')
# Note: the default order of color for cv2 is BGR
# A convert is needed if interacted with other software 
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)

# Note: the (x,y) of cv2.imread is different from numpy
y_size = img.shape[0]
x_size = img.shape[1]
img = cv2.resize(img, dsize=(int(x_size/6), int(y_size/6)))
img = img[:,:,2]
print(img.shape)
cv2.imshow('img', img)
cv2.imwrite('./img/img_resized.jpg', img)

# Note: the size of the kernel must be odd numbers
img_Guassian = cv2.GaussianBlur(img, (9,9), 0.5)
cv2.imshow('img_Guassian', img_Guassian)
cv2.imwrite('./img/img_Guassian.jpg', img_Guassian)

# Derivation of the 1st order in direction x
img_Sobel = cv2.Sobel(img_Guassian, cv2.CV_16S, 1, 0)
# Convert back to unit8
img_Sobel = cv2.convertScaleAbs(img_Sobel)
cv2.imshow('img_Sobel', img_Sobel)
cv2.imwrite('./img/img_Sobel.jpg', img_Sobel)
cv2.waitKey()
