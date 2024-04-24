import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def hough(fname):
    #init
    bgr = cv2.imread(fname)
    img = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 5)
    width = img.shape[1]
    height = img.shape[0]
    #Hough
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT_ALT,1,20,param1=50,param2=0.8)
    #print(str(circles))
    #vykreslovani na puvodni obrazek pomoci Pillow, imo jednodussi nez pyplot
    count=len(circles[0,:])
    wimg = Image.open(fname)
    I1 = ImageDraw.Draw(wimg)
    font=ImageFont.truetype("arial.ttf", 60)
    I1.text(((width/2)-25, (height/2)-30), str(count),font=font, fill=(0,255,0))
    wimg.show()

def erode(fname):
    #init
    img = np.uint8(cv2.imread(fname, cv2.IMREAD_GRAYSCALE)/255)
    kernel = np.ones((3,3),np.uint8)
    height = int(img.shape[0]/2)
    halfs = [img[:height, :], img[height:,:]]
    plot_pos = 1

    for garbage, half in enumerate(halfs):
        #print("test")
        cycles=0
        eroded = half.copy()
        #eroduje dokud muze
        while True:
            temp = cv2.erode(eroded, kernel)
            check = len(np.column_stack(np.where(temp != 0)))
            #print(str(check))
            if check==0:
                break
            cycles+=1
            eroded=temp
        coords = np.column_stack(np.where(eroded!=0))
        #vykreslovani erozi
        plt.subplot(2,2,plot_pos)
        plt.title("souradnice eroze " + str(plot_pos) + " : " + str(coords))
        plt.imshow(eroded, cmap="gray")
        #dilace
        dilated=cv2.dilate(eroded, kernel, iterations=cycles)
        plt.subplot(2,2,(plot_pos+2))
        plt.title("dilace "+str(plot_pos))
        plt.imshow(dilated, cmap="gray")

        plot_pos+=1
    plt.show()

if __name__ == "__main__":
    hough("Cv11_c06.bmp")
    erode("Cv11_merkers.bmp")
