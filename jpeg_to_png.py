import cv2

img = cv2.imread('wr.png')
img = cv2.fastNlMeansDenoisingColored(img, img,1,1,1,31)

a_img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)

for r in range(len(a_img)):
    for c in range(len(a_img[0])):
        p = a_img[r][c]
    #     print(p, "this is p!!")
    #     break
    # break
        if p[0] == 254 and p[1] == 254 and p[2] == 254:
            p[3] = 0
            # print(a_img[r][c], r, c)
        else:
            p[0] = 0
            p[1] = 0
            p[2] = 0
            p[3] = 255

cropped = a_img[:-20][:]

print(50*"-")
print("filtering and alpha channel addition complete")
print(50*"-")
alpha_img = cv2.imwrite('alpha_wr.png', cropped)

