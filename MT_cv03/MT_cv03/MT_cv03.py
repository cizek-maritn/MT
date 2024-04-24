import cv2
import numpy as np
import matplotlib.pyplot as plt
import struct

def imread_test():
    bgr=cv2.imread('cv03_objekty1.bmp')
    print(str(bgr))
    rgb=cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    h=bgr.shape[0]
    w=bgr.shape[1]
    plt.imshow(bgr)
    plt.colorbar()
    plt.show()

def image_read(filename):
    #cteni hlavicky
    f=open(filename, 'rb')
    f.read(18)
    w=struct.unpack('i', f.read(4))[0]
    h=struct.unpack('i', f.read(4))[0]
    f.read(2)
    bpp=struct.unpack('h', f.read(2))[0]
    #print(str(w)+" "+str(h)+" "+str(bpp))
    rgb=np.zeros((w,h,3), dtype=int)
    #bgr=np.zeros((w,h,3))
    f.read(24)
    #offset na konci radku
    offset=4-(w%4)
    #print(str(offset))
    #nacitani dat
    for i in range(w):
        for j in range(h):
            rgb[w-i-1][j][2]=struct.unpack('B', f.read(1))[0]
            rgb[w-i-1][j][1]=struct.unpack('B', f.read(1))[0]
            rgb[w-i-1][j][0]=struct.unpack('B', f.read(1))[0]
        f.read(4-offset)
    #print(str(rgb))
    #testcv = cv2.imread(filename)
    #print("abc")
    #print(str(testcv))
    #plt.imshow(rgb)
    #plt.show()
    return rgb, w, h

def showGray(rgb):
    imgFloat=np.float32(rgb)
    gray=cv2.cvtColor(imgFloat, cv2.COLOR_RGB2GRAY)
    plt.figure("grayscale")
    plt.subplot(1, 2, 1)
    plt.imshow(rgb)
    plt.title("RGB")
    plt.subplot(1,2,2)
    plt.imshow(gray, cmap="gray")
    plt.title("GRAYSCALE")
    plt.show()
    print("showing grayscale")

def showHsv(rgb):
    imgFloat=np.float32(rgb)
    hsv=cv2.cvtColor(imgFloat, cv2.COLOR_RGB2HSV)
    plt.figure("HSV")
    plt.subplot(2,2,1)
    plt.imshow(rgb)
    plt.title("RGB")
    plt.subplot(2,2,2)
    plt.imshow(hsv[:,:,0], cmap="jet")
    plt.title("H")
    plt.colorbar()
    plt.subplot(2,2,3)
    plt.imshow(hsv[:,:,1], cmap="jet")
    plt.title("S")
    plt.colorbar()
    plt.subplot(2,2,4)
    plt.imshow(hsv[:,:,2], cmap="jet")
    plt.title("V")
    plt.colorbar()
    #print(str(hsv))
    plt.show()
    print("showing hsv")

def showYcrcb(rgb):
    imgFloat=np.float32(rgb)
    bgr=cv2.cvtColor(imgFloat, cv2.COLOR_RGB2BGR)
    ycrcb=cv2.cvtColor(bgr, cv2.COLOR_BGR2YCR_CB)
    plt.figure("YCRCB")
    plt.subplot(2,2,1)
    plt.imshow(rgb)
    plt.title("RGB")
    plt.subplot(2,2,2)
    plt.imshow(ycrcb[:,:,0], cmap="gray")
    plt.title("Y")
    plt.colorbar()
    plt.subplot(2,2,3)
    plt.imshow(ycrcb[:,:,1], cmap="jet")
    plt.title("CR")
    plt.colorbar()
    plt.subplot(2,2,4)
    plt.imshow(ycrcb[:,:,2], cmap="jet")
    plt.title("CB")
    plt.colorbar()
    plt.show()
    print("showing ycrcb")

def prahovani(bgr):
    rgb=cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    prahRGB=rgb.copy()
    h=rgb.shape[0]
    w=rgb.shape[1]
    for i in range(w):
        for j in range(h):
            row=rgb[j][i]
            red=int(row[0])
            green=int(row[1])
            blue=int(row[2])
            try:
                r=red / (red + green + blue)
                if r<0.5:
                    prahRGB[j][i][0]=255
                    prahRGB[j][i][1]=255
                    prahRGB[j][i][2]=255
            except:
                prahRGB[j][i][0]=255
                prahRGB[j][i][1]=255
                prahRGB[j][i][2]=255
                continue
    plt.figure("prahovani")
    plt.subplot(1, 2, 1)
    plt.imshow(rgb)
    plt.title("RGB")
    plt.subplot(1,2,2)
    plt.imshow(prahRGB)
    plt.title("r>0.5")
    plt.show()
    print("showing prahovani")

if __name__ == "__main__":
    #imread_test()
    data, width, height=image_read('cv03_objekty1.bmp')
    showGray(data)
    showHsv(data)
    showYcrcb(data)
    jpgData=cv2.imread("cv03_red_object.jpg")
    prahovani(jpgData)
    print("done")

