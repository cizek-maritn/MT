import cv2
import numpy as np
import matplotlib.pyplot as plt
import struct

def load_image(img_path):
    bgr=cv2.imread(img_path)
    rgb=cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    #print(rgb)
    return rgb

def correction(img, etal):
    width=img.shape[1]
    height=img.shape[0]
    new_img=np.zeros((height,width,3), dtype=int)
    for i in range(width):
        for j in range(height):
            red=img[j][i][0]
            green=img[j][i][1]
            blue=img[j][i][2]
            gray=etal[j][i][0]
            if (gray==0):
                gray=1
            new_red=(red/255)/(gray/255)
            new_green=(green/255)/(gray/255)
            new_blue=(blue/255)/(gray/255)
            new_img[j][i][0]=int(new_red*255)
            new_img[j][i][1]=int(new_green*255)
            new_img[j][i][2]=int(new_blue*255)
    return new_img
            
def get_hist(img):
    histogram=cv2.calcHist([img], [0], None, [256], [0,256])
    #print(str(histogram))
    return histogram

def hist_aprox(img, hist):
    width=img.shape[1]
    height=img.shape[0]
    new_img=img.copy()
    q0=0
    qk=255
    for x in range(width):
        for y in range(height):
            intensity=img[y,x,0]
            hist_inten=[int(x) for x in hist[0:intensity]]
            new_img[y,x]=((qk-q0)/(width*height))*sum(hist_inten)
    return new_img


if __name__ == "__main__":
    err1=load_image("Cv04_porucha1.bmp")
    etal1=load_image("Cv04_porucha1_etalon.bmp")
    fix1=correction(err1, etal1)
    plt.figure("First")
    plt.subplot(1,3,1)
    plt.imshow(err1)
    plt.subplot(1,3,2)
    plt.imshow(etal1)
    plt.subplot(1,3,3)
    plt.imshow(fix1)
    plt.show()
    err2=load_image("Cv04_porucha2.bmp")
    etal2=load_image("Cv04_porucha2_etalon.bmp")
    fix2=correction(err2, etal2)
    plt.figure("Second")
    plt.subplot(1,3,1)
    plt.imshow(err2)
    plt.subplot(1,3,2)
    plt.imshow(etal2)
    plt.subplot(1,3,3)
    plt.imshow(fix2)
    plt.show()
    rentgen=load_image("Cv04_rentgen.bmp")
    hist=get_hist(rentgen)
    plt.figure("Third")
    plt.subplot(2,2,1)
    plt.imshow(rentgen)
    plt.subplot(2,2,2)
    plt.plot(hist)
    new_rentgen=hist_aprox(rentgen, hist)
    plt.subplot(2,2,3)
    plt.imshow(new_rentgen)
    new_hist=get_hist(new_rentgen)
    plt.subplot(2,2,4)
    plt.plot(new_hist)
    plt.show()
    print("done")
