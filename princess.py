from PIL import Image

##FUNCTIONS
def colorSwitcher(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    darkBlue = (0,51,76)
    darkRed = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)

def intensityFunc (red,green,blue):
    intensity = red + green + blue
    darkBlue = (0,51,76)
    darkRed = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)
    if intensity <= 182:
        newPixelList.append(darkBlue)
    elif intensity >= 182 and intensity <= 364:
        newPixelList.append(darkRed)
    elif intensity >= 364 and intensity <= 546:
        newPixelList.append(lightBlue)
    elif intensity >= 546:
        newPixelList.append(yellow)

#RUNNING CODE
myImage = Image.open("sleepingBeauty.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    intensityFunc(red,green,blue)

newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show("sleepingBeauty.jpg")


