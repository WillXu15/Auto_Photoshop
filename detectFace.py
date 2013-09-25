import cv2
import math
import numpy as np

def main():
	cascade = cv2.CascadeClassifier()

	cascade.load("haarcascades/haarcascade_frontalface_default.xml")

	img = cv2.imread("face.jpg")

	answer = cascade.detectMultiScale(img)

	if len(answer) != 0:
		for i in answer:
			clearFace(img, i[0], i[1], i[2], i[3], (255,0,0))

#if len(answer) != 0:
#	for i in answer:
#		cv2.rectangle(img, (i[0], i[1]),(i[0]+i[2], i[1]+ i[3]), (255,0,0) )

	#cv2.imshow("",img)
	#cv2.waitKey()
	#cv2.destroyWindow("")

def clearFace(img, x, y, length, width, color = (255,0,0)):
	arr = []
	for i in range(y, y+width):
		for j in range(x, x+length):
			arr.append( (img[j][i][0], img[j][i][1], img[j][i][2]) )
	color = np.median(np.array(arr), axis = 0)
	threshold = math.sqrt(color[0]**2 + color[1]**2 + color[2]**2)
	print "threshold = %d" %threshold
	notInThreshold = []
	for i in range(y, y+width):
		for j in range(x, x+length):
			num = math.sqrt(img[j][i][0]**2+img[j][i][2]**2+img[j][i][1**2])
			if (not num<threshold-20) or (not num>threshold+20):
				notInThreshold.append(img[j][i])
	print len(notInThreshold), x*y
	#if colors are within threshold, go on
	#if color is not within threshold, add to array and then continue
	#after all locations are added into array, traverse through array and normalize colors

if __name__ == "__main__": main()







