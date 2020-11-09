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