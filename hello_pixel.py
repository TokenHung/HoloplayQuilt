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
frame_index = 0
fps = 15
# assign a blank canvas
blank_image = np.zeros((height, width, 3), np.uint8)
seconds = 0
cur_seconds = 0
RawImgPath = "RawPng/Toy/"

def main():
    jpg_save(RawImgPath, img, jpg_quality=10)
    
    sampling_interval = input_image_num // PARALLAX
    # imread for 45 parallax
    for seconds in range(0, 10):
        j = 0
        for frame_index in range(1,fps +1):
            if (seconds % 2 == 0):
                frame_modify = frame_index
            else:
                frame_modify = fps -j
            j = j + 1
            for i in range(1, PARALLAX + 1):
                index_for_feed_image = (i + parallax_per_pic - 1) // parallax_per_pic

                feed_image = 1 + (index_for_feed_image - 1) * sampling_interval * parallax_per_pic + (frame_modify -1)

                if (feed_image >= 100):
                    feed_image_str = str(feed_image)
                elif (100 > feed_image and feed_image >= 10):
                    feed_image_str = "0" + str(feed_image)
                else:
                    feed_image_str = "00" + str(feed_image)
                
                # for debugging
                # img = cv.imread("./Label/" + "00" + str(feed_image_str) + ".png")

                img = cv.imread(RawImgPath + "0" + feed_image_str + ".png")
                print ("str feed: " + feed_image_str)
                
                canvas_paint(img, i, seconds)

            cv.imwrite("frame/Tile_generate__" + str(seconds * 15 + frame_index) + ".png", blank_image)


def canvas_paint(img, i, seconds):
    print("******debugging, index: " + str(i))
    # img = cv.resize(img ,(tile_width, tile_height))
    # fake zoom in 
    #img = cv.resize(img ,(tile_width + seconds * 5, tile_height + seconds * 5))
    #crop_img = img[0 + seconds * 5 : tile_height + seconds * 5, 0 + seconds * 5 : tile_width + seconds * 5].copy()
        
    img = cv.resize(img ,(tile_width, tile_height))
    j = i % 5 if (i % 5 != 0) else 5
    k = i // 5 if (i % 5 != 0) else i // 5 -1
    
    blank_image[k * tile_height : (k + 1) * tile_height, ((i - 1) % 5) * tile_width : j * tile_width] = img

    # cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    # cv.imshow("Preview", img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

def jpg_save(path, image, jpg_quality=None, png_compression=None):
    '''
    persist :image: object to disk. if path is given, load() first.
    jpg_quality: for jpeg only. 0 - 100 (higher means better). Default is 95.
    png_compression: For png only. 0 - 9 (higher means a smaller size and longer compression time).
                    Default is 3.
    '''
    if (jpg_quality):
        cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
    elif png_compression:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
    else:
        cv2.imwrite(path, image)

if __name__ == '__main__':
    main()
