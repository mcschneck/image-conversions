**addAlpha(img)**

adds alpha channel to rgb image
default transparency is opaque (255)

**convertRGBAtoBWA(img, threshold=None, alpha=None)**

inputs: 4 channel color image, threshold array of (len = 3, i.e. [r, g, b]), alpha array (len = 2, [white alpha, black alpha])
returns: 4 channel binary image

takes 4 channel color image and converts to 4 channel black and white image (binary image)
pixels darker than threshold values are turned to black and opaque
pixels lighter than threshold values are turned to white and transparent

choosing threshold values:
- pixels with values greater than threshold will be converted to white pixels with transparent alpha channels
- pixels with values less than threshold will be converted to black pixels with opaque alpha channels

**easyRGBAtoBWA(img)**

inputs: 4 channel color image
returns: 4 channel binary image

doesn't require a threshold array and therefore doesn't need as much code
prevents user from having to make decisions
    
    
