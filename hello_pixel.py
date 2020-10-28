import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# GLOBAL
# Ultimate input would be (PARALLAX_PER_PIC, height, width, horizontal_tile_num, vertical_tile_num)
PARALLAX = 45
parallax_per_pic = 2
height = 4096
width = 4096
input_image_num = 90
tile_width = 4096 // 5
tile_height = 4096 // 9

# assign a blank canvas
blank_image = np.zeros((height, width, 3), np.uint8)

def main():
    # Try samling
    # sampling_interval = input_image_num // PARALLAX
    sampling_interval = input_image_num // PARALLAX

    # imread for 45 parallax
    for i in range(1, PARALLAX + 1):
        index_for_feed_image = (i + parallax_per_pic - 1) // parallax_per_pic
        # feed_image = index_for_feed_image + (index_for_feed_image - 1) * sampling_interval * parallax_per_pic
        feed_image = 1 + (index_for_feed_image - 1) * sampling_interval * parallax_per_pic
        # feed_image_str = feed_image >= 10 ? str(feed_image) : "0" + str(feed_image)
        if (feed_image >= 10):
            feed_image_str = str(feed_image)
        else:
            feed_image_str = "0" + str(feed_image)
        
        # read img
        img = cv.imread("./Label/" + "00" + str(feed_image_str) + ".png")

        print ("str feed: " + str(feed_image_str))

        canvas_paint(img, i)
    cv.imwrite("Tile_generate_L.png", blank_image)


def canvas_paint(img, i):
    print("******debugging, index: " + str(i))
    # cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    #cv.imshow("aaa", img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    img = cv.resize(img ,(tile_width, tile_height))

    # j = (i % 5 == 0)? 5 : i % 5
    j = i % 5 if (i % 5 != 0) else 5
    k = i // 5 if (i % 5 != 0) else i // 5 -1
    
    blank_image[k * tile_height : (k + 1) * tile_height, ((i - 1) % 5) * tile_width : j * tile_width] = img

    '''Old######################################### 
        if (i * sample < 10):
            img = cv.imread("000" + str(i * sample) + ".png")
        else:
            img = cv.imread("00" + str(i * sample) + ".png")
        

        # debugging
        print("now " + str(i))

        # j = (i % 5 == 0)? 5 : i % 5
        j = i % 5 if (i % 5 != 0) else 5
        k = i // 5 if (i % 5 != 0) else i // 5 -1
        blank_image[k * tile_height : (k + 1) * tile_height, ((i - 1) % 5) * tile_width : j * tile_width] = img
        #blank_image[((i-1) % 5) * tile_width : (i % 5) * tile_width, ((i-1) % 9) * tile_height : (i % 9) * tile_height] = img
        #plt.imshow(img)
        #plt.show()
        #img = cv.imread("00.png')
    '''

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
