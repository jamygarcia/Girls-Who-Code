from PIL import Image


##FUCTIONS



#Import the image and make the pixel
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList =[]

length = len(pixelList)
halfway = length//2

counter = 0



def negative(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

#find the new red, green, and blue

    newRed = 255 - red
    newGreen = 255 - green
    newBlue = 255 - blue

    p = (newRed, newGreen, newBlue)
    newPixelList.append(p)





def overExpose(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    newRed=red*2
    if newRed >255:
        newRed = 255

    newGreen=green*2
    if newGreen >255:
        newGreen = 255
    
    newBlue=blue*2
    if newBlue >255:
        newBlue = 255
        
    p = (newRed,newGreen,newBlue)

    #add pixel to new pixel list
    newPixelList.append(p)


        

for pixel in pixelList:
    if (counter <= halfway):
        overExpose(pixel)
    else:
        negative(pixel)
    counter += 1

#open the image
newImage = Image.new("RGB", myImage.size)
newImage.putdata(newPixelList)
newImage.show()

