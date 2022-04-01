import cv2

def addAlpha(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)

def convertRGBAtoBWA(img, threshold=None, alpha=None):
    '''
    takes 4 channel color image and converts to 4 channel black and white image (binary image)
    pixels darker than threshold values are turned to black and opaque
    pixels lighter than threshold values are turned to white and transparent

    choosing threshold values:
        pixels with values greater than threshold will be converted to white pixels with white alpha channel
        pixels with values less than threshold will be converted to black pixels with black alpha channel
    
    choosing alpha values:
        first alpha values changes white pixels
        second alpha value changes black pixels

    inputs: 4 channel color image, threshold array (len = 3), alpha array (len = 2)
    returns: 4 channel binary image
    '''
    #default values for thresholds
    rt = 125
    gt = 125
    bt = 125

    wa = 0
    ba = 255

    if threshold != None:
        assert len(threshold) == 3, "threshold should be a list of 3 arguments (rgb thresholds)"
        rt = threshold[0]
        gt = threshold[1]
        bt = threshold[2]

    if alpha != None:
        assert len(alpha) == 2, "alpha should be a list of 2 arguments (white and black alphas)"
        wa = alpha[0]
        ba = alpha[1]

    for r in range(len(img)):
        for c in range(len(img[0])):
            p = img[r][c]
            if p[0] >= rt and p[1] >= gt and p[2] >= bt:
                # make lighter pixels white and transparent
                p[0] = 255
                p[1] = 255
                p[2] = 255
                p[3] = wa
            else:
                # make darker pixels black and opaque
                p[0] = 0
                p[1] = 0
                p[2] = 0
                p[3] = ba
    return img

def easyRGBAtoBWA(img):
    return convertRGBAtoBWA(img, threshold=None)

def hasAlphaConvertRGBtoBW(img, threshold):
    '''
    takes color image and converts to black and white without changing alpha

    choosing threshold values:
        pixels with values greater than threshold will be converted to white pixels
        pixels with values less than threshold will be converted to black pixels

    inputs: 4 channel img
    '''
    rt = 125
    gt = 125
    bt = 125

    if threshold != None:
        assert len(threshold) == 3, "threshold should be a list of 3 arguments (rgb thresholds)"
        rt = threshold[0]
        gt = threshold[1]
        bt = threshold[2]

    for r in range(len(img)):
        for c in range(len(img[0])):
            p = img[r][c]
            if p[0] >= rt and p[1] >= gt and p[2] >= bt:
                # make lighter pixels white and transparent
                p[0] = 255
                p[1] = 255
                p[2] = 255
            else:
                # make darker pixels black and opaque
                p[0] = 0
                p[1] = 0
                p[2] = 0
                
    return img

