import cv2
import numpy as np

def main():
	cascade = cv2.CascadeClassifier()

	cascade.load("haarcascades/haarcascade_frontalface_default.xml")

	img = cv2.imread("photo.jpg")

	answer = cascade.detectMultiScale(img)

#	if len(answer) != 0:
#		for i in answer:
#			clearFace(img, i[0], i[1], i[2], i[3], (255,0,0))
	if len(answer) != 0:
		for i in answer:
			contours(img)
#	if len(answer) != 0:
#		for i in answer:
#			cv2.rectangle(img, (i[0], i[1]),(i[0]+i[2], i[1]+ i[3]), (255,0,0) )

#		cv2.imshow("",img)
#		cv2.waitKey()
#		cv2.destroyWindow("")

def contours(img):
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	redThresh = cv2.inRange(hsv, np.array((0,0,0)), np.array((10,100,100)))
	erode = cv2.erode(redThresh, None, iterations = 3)
	dilate = cv2.dilate(erode, None, iterations =10)
	contours,hierarchy = cv2.findContours(redThresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	for cnt in contours:
		x,y,w,h = cv2.boundingRect(cnt)
		cv2.rectangle(img, (x,y), ((x+w),(y+h)),[0,255,0],2)
	cv2.imwrite("output.jpg", img)

def clearFace(img, x, y, length, width, kolor = (255,0,0)):
	N = 5
	arr = []
	ThreshNum = 150
	for i in range(y, y+width):
		for j in range(x, x+length):
			arr.append( (img[j][i][0], img[j][i][1], img[j][i][2]) )
	color = np.median(np.array(arr), axis = 0)
	rThresh = color[0]
	gThresh = color[1]
	bThresh = color[2]
	print "threshold = %d %d %d" %(rThresh,gThresh,bThresh)
	notInThreshold = []
	for i in range(y, y+width):
		for j in range(x, x+length):
			if abs(img[j][i][0]-rThresh)>ThreshNum or abs(img[j][i][1]-gThresh)>ThreshNum or abs(img[j][i][2]-bThresh)>ThreshNum:
				notInThreshold.append((j,i))
	print len(notInThreshold), width*length
	for i in range(len(notInThreshold)):
		cv2.circle(img, (notInThreshold[i][0], notInThreshold[i][1]), 1, (255,0,0))
	cv2.imwrite("output.jpg", img)
	#if colors are within threshold, go on
	#if color is not within threshold, add to array and then continue
	#after all locations are added into array, traverse through array and normalize colors

if __name__ == "__main__": main()







