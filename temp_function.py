import cv2 as cv
import numpy as np
RawImgPath = "RawPng/DSLF - Castle/"
def main():
      
  frame = cv.imread(RawImgPath + "0001.png")

  ret,buf=cv.imencode("toto.jpg",frame, [int(cv.IMWRITE_JPEG_QUALITY), 10])
  #bufjpg = bytearray(buf)
  #fs = open("toto2.jpg", "wb")
  #fs.write(bufjpg)
  #print (str(buf[0:15]))
  img=cv.imdecode(buf,cv.IMREAD_COLOR)
  cv.imshow("img",img)
  cv.waitKey(0)

def jpg_save(path, image, jpg_quality=None, png_compression=None):
  '''
  persist :image: object to disk. if path is given, load() first.
  jpg_quality: for jpeg only. 0 - 100 (higher means better). Default is 95.
  png_compression: For png only. 0 - 9 (higher means a smaller size and longer compression time).
                  Default is 3.
  '''
  if jpg_quality:
    cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
  elif png_compression:
    cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
  else:
    cv2.imwrite(path, image)



if __name__ == "__main__":
    main()