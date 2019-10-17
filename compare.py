#from skimage.measure import structural_similarity as ssim
from skimage import measure
from skimage.transform import resize
from imutils import paths
from pathlib import Path
from scipy import misc
import argparse
import imutils
import matplotlib.pyplot as plt
import numpy as np
import cv2


def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float"))**2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err

def compare_images(imageA, imageB):
	m = mse(imageA, imageB)
	s = measure.compare_ssim(imageA, imageB,multichannel=True)

	#print out the results
	print("MSE: %.2f, SSIM: %.2f" % (m, s))

def shorten_path(file_path, length):
	return Path(*Path(file_path).parts[-length:])

Filelost = 0

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--original", type=str, required=True,
	help="path to input directory of original images")

ap.add_argument("-ii", "--copy", type=str, required=True,
	help="path to input directory of copied images")



#ap.add_argument("-o", "--output", type=str, required=True,
#	help="path to the output image")
args = vars(ap.parse_args())
# grab the paths to the input images and initialize our images list
print("[INFO] loading images...")

imagePaths1 = sorted(list(paths.list_images(args["original"])))
imagePaths2 = sorted(list(paths.list_images(args["copy"])))

# loop over the image paths, load each one, and add them to our
# images to stitch list

for imagePath in imagePaths1:
	p1 = shorten_path(imagePath,1)
	for imagePathb in imagePaths2:
		p2 = shorten_path(imagePathb,1)
		if p1 == p2:
			imga = cv2.imread(imagePath)
			imgb = cv2.imread(imagePathb)
			print("File Name: "+str(p1))
			compare_images(misc.imresize(imga, (64, 64)),misc.imresize(imgb, (64, 64)))
			break


print("File Loss = %d" % (len(imagePaths1)-len(imagePaths2)))





	
