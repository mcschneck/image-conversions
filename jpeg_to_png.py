import cv2
import lib

img = cv2.imread('line-corn-logo.jpeg')
img = cv2.fastNlMeansDenoisingColored(img, img,1,1,1,31)
a_img = lib.addAlpha(img)

# bw_aimg = lib.easyRGBAtoBWA(img)

# cropped = bw_aimg[:-20][:]

# print(50*"-")
# print("filtering and alpha channel addition complete")
# print(50*"-")
# alpha_img = cv2.imwrite('alpha_wr.png', cropped)

