import os
import numpy
import cv2
import sys

class negGenerator:
	def __init__ (self, srcImgPath, w, h, mode = 'mono'):
		srcImg = None
		width = None
		height = None
		w = int(w)
		h = int(h)
		if mode is 'color':
			srcImg = cv2.imread(srcImgPath, 1)
			height, width, dummy = srcImg.shape
		elif mode is 'mono':
			srcImg = cv2.imread(srcImgPath, 0)
			height, width = srcImg.shape

		wRatio = width / w
		hRatio = height / h
		if wRatio <= 1 or hRatio <= 1:
			raw_input('srcImg too small or outImg too large\n')
		else:
			re = raw_input ('to create %s images, sure? (y/n?) ' %(wRatio * hRatio))
			if re is 'y' or re is 'Y' or re is '':
				if not os.path.exists('out'):
					os.makedirs('out')
				for i in range(0,hRatio):
					for j in range(0,wRatio):
						cv2.imwrite('out/out%s.jpg' %(i * wRatio + j), srcImg[i * h : (i + 1) * h  , j * w : (j + 1) * w])
				raw_input('done\n')
			else: 
				sys.exit()


if __name__ == '__main__':

	scrImgPath = raw_input('scrImgPath ')
	w = raw_input('width of cropped image ')
	h = raw_input('height of cropped image ')
	myNegGenerator = negGenerator(scrImgPath,w,h)

