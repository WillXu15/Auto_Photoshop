import cv2

cascade = cv2.CascadeClassifier()

cascade.load("haarcascades/haarcascade_frontalface_default.xml")

img = cv2.imread("face.jpg")

answer = cascade.detectMultiScale(img)

if len(answer) != 0:
	for i in answer:
		cv2.rectangle(img, (i[0], i[1]),(i[0]+i[2], i[1]+ i[3]), (255,0,0) )

cv2.imshow("",img)
cv2.waitKey()
cv2.destroyWindow("")
