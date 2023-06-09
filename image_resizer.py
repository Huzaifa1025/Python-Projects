import cv2

image = cv2.imread("lion.jpeg", cv2.IMREAD_UNCHANGED)
#cv2.imshow("title", image)


scale_percent = 50 #percentage by which image is resized

#Calculate the new dimensions of image
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

output = cv2.resize(image , (new_width, new_height))

cv2.imwrite('newImage.jpeg', output)
cv2.waitKey(0)