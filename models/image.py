from PIL import Image

class ImBtn():
    def couper_image(image):
        '''
        function to cut an image into 16 tiles
        :return: 16 images with the right dimensions
        '''
        image = Image.open(image)

        la, lo = image.size #we get the size of the image
        center_x, center_y = la//2, lo//2 #take the center point of the width and length
        size = min(la, lo) #we take the minimum size between width and length to be able to make a square

        #coordinates for cutting the new square
        left = center_x - size//2 
        top = center_y - size//2
        right = center_x + size//2
        bottom = center_y + size//2

        image = image.crop((left, top, right, bottom)) #get a square image
        image = image.resize((600, 600))#resize

        x,y = image.size
        nw_image = Image.new("RGB", (x,y), (0,0,0,0)) #new image
        
        for i in range(600):
            for j in range(600):
                c, d, e = image.getpixel((i,j))
                nw_image.putpixel((i,j),(c,d,e))  #we fill in the new small images
        nw_image.crop((0,0,x/4,y/4)).save('img/image1.jpg') #we save the 16 images
        nw_image.crop((x/4,0,x/2,y/4)).save('img/image2.jpg')
        nw_image.crop((x/2,0,3*x/4,y/4)).save('img/image3.jpg')
        nw_image.crop((3*x/4,0,x,y/4)).save('img/image4.jpg')
        nw_image.crop((0,y/4,x/4,y/2)).save('img/image5.jpg')
        nw_image.crop((x/4,y/4,x/2,y/2)).save('img/image6.jpg')
        nw_image.crop((x/2,y/4,3*x/4,y/2)).save('img/image7.jpg')
        nw_image.crop((3*x/4,y/4,x,y/2)).save('img/image8.jpg')
        nw_image.crop((0,y/2,x/4,3*y/4)).save('img/image9.jpg')
        nw_image.crop((x/4,y/2,x/2,3*y/4)).save('img/image10.jpg')
        nw_image.crop((x/2,y/2,3*x/4,3*y/4)).save('img/image11.jpg')
        nw_image.crop((3*x/4,y/2,x,3*y/4)).save('img/image12.jpg')
        nw_image.crop((0,3*y/4,x/4,y)).save('img/image13.jpg')
        nw_image.crop((x/4,3*y/4,x/2,y)).save('img/image14.jpg')
        nw_image.crop((x/2,3*y/4,3*x/4,y)).save('img/image15.jpg')
        nw_image.crop((3*x/4,3*y/4,x,y)).save('img/image16.jpg')
        # return nw_image


