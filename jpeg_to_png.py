import cv2
import lib

# img = cv2.imread('line-corn-logo.jpeg')
# img = cv2.fastNlMeansDenoisingColored(img, img,1,1,1,31)
# a_img = lib.addAlpha(img)

colorimg = cv2.imread('wrbus.JPG')
colorimg = cv2.fastNlMeansDenoisingColored(colorimg, colorimg,1,1,1,31)
colorimg = lib.addAlpha(colorimg)

# bw_aimg = lib.easyRGBAtoBWA(img)

# cropped = bw_aimg[:-20][:]
colorimg = lib.makeTransparentBackground(colorimg)
print(50*"-")
print("filtering and alpha channel addition complete")
print(50*"-")
colorimg = cv2.imwrite('wrbus.png', colorimg)

