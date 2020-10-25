import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
def main():
    height = 360
    width = 1920
    pixel_number = height * width
    blank_image = np.zeros((height,width,3), np.uint8)
    #
    # cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    for i in range(1):
        for j in range(4):
            if(i == 0 and j == 0):
                continue
            img = cv.imread("00"+str(i)+str(j)+".png")
            img = cv.resize(img ,(640,360))
            print(j)
            blank_image[:,(j-1)*640:(j)*640] = img
            #plt.imshow(img)
            #plt.show()
        #img = cv.imread("00.png')    
    cv.imshow("aaa", blank_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    
    '''
    px = img[100, 100]
    print(px)
    # get px's BGR
    # get [157 166 200]

    # accessing only blue pixel
    # 0 = B, 1 = G , 2 = R
    blue = img[100, 100, 0]
    print(blue)
    # get 157

    #img[100, 100] = [255, 255, 255]
    print(img[100, 100])
    # get [255 255 255]
    '''
    
    '''
    # accessing RED value
    img.item(10,10,2)
    # get 59
    
    # modifying RED value
    img.itemset((10,10,2),100)
    img.item(10,10,2)
    # get 100
    '''
    '''
    # Accessing image properties
    print (img.shape)

    # total pixel
    print(img.size)
    
    # data type
    print(img.dtype)
    '''

    '''
    extract ROI or assign ROI
    ball = img[280:340, 330:390]
    img[273:333, 100:160] = ball
    '''
if __name__ == '__main__':
    main()
