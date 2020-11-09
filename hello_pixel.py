import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# GLOBAL
# Ultimate input would be (PARALLAX_PER_PIC, height, width, horizontal_tile_num, vertical_tile_num)
PARALLAX = 45
parallax_per_pic = 1
height = 4096
width = 4096
input_image_num = 180
tile_width = 4096 // 5
tile_height = 4096 // 9
frame_index = 1
fps = 15
# assign a blank canvas
blank_image = np.zeros((height, width, 3), np.uint8)
seconds = 10
cur_seconds = 0

def main():
    sampling_interval = input_image_num // PARALLAX
    # imread for 45 parallax
    for frame_index in range(1,16):
        for i in range(1, PARALLAX + 1):
            index_for_feed_image = (i + parallax_per_pic - 1) // parallax_per_pic
            feed_image = 1 + (index_for_feed_image - 1) * sampling_interval * parallax_per_pic + frame_index

            if (feed_image >= 100):
                feed_image_str = str(feed_image)
            elif (100 > feed_image and feed_image >= 10):
                feed_image_str = "0" + str(feed_image)
            else:
                feed_image_str = "00" + str(feed_image)
            
            # for debugging
            # img = cv.imread("./Label/" + "00" + str(feed_image_str) + ".png")

            img = cv.imread("0" + feed_image_str + ".png")
            print ("str feed: " + feed_image_str)

            canvas_paint(img, i, cur_seconds)
        
        cv.imwrite("frame/Tile_generate_" + str(frame_index) + ".png", blank_image)

def canvas_paint(img, i, cur_seconds):
    print("******debugging, index: " + str(i))
    # cur_playtime = frame_fps
    # img = cv.resize(img ,(tile_width, tile_height))
    # fake zoom in 
    
    img = cv.resize(img ,(tile_width + cur_seconds * 5, tile_height + cur_seconds * 5))
    crop_img = img[0 + cur_seconds * 5 : tile_height + cur_seconds * 5, 0 + cur_seconds * 5 : tile_width + cur_seconds * 5].copy()

    j = i % 5 if (i % 5 != 0) else 5
    k = i // 5 if (i % 5 != 0) else i // 5 -1
    
    blank_image[k * tile_height : (k + 1) * tile_height, ((i - 1) % 5) * tile_width : j * tile_width] = crop_img

    # cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    # cv.imshow("Preview", img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

if __name__ == '__main__':
    main()
