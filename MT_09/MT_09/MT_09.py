import cv2
import numpy as np
import matplotlib.pyplot as plt

def loadImage(fname):
    bgr = cv2.imread(fname)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    return rgb

def PCA(img):
    #rozmery matice, M - pocet kanalu, N - rozmer obrazku
    width=img.shape[1]
    height=img.shape[0]
    M=3
    N=width*height
    #print(str(N))
    redList = []
    greenList = []
    blueList = []
    #ziskavani rgb hodnot
    for i in range(width):
        for j in range(height):
            red=img[j][i][0]
            green=img[j][i][1]
            blue=img[j][i][2]
            redList.append(red)
            greenList.append(green)
            blueList.append(blue)
    #rgb listy na array
    print("step 1 - done")
    redArr = np.array(redList)
    greenArr = np.array(greenList)
    blueArr = np.array(blueList)
    #stredni vektor
    avgList = []
    for i in range(N):
        #musim prevest na python int abych predesel overflow
        avgVal = int((int(redArr[i])+int(greenArr[i])+int(blueArr[i]))/3)
        avgList.append(avgVal)
    avgArr = np.array(avgList)
    print("step 2 - done")
    #vektory w
    redw = np.subtract(redArr, avgArr)
    greenw = np.subtract(greenArr, avgArr)
    bluew = np.subtract(blueArr, avgArr)
    print("step 3 - done")
    #vytvoreni matice W
    arrayW = np.array([redw, greenw, bluew])
    print(str(arrayW.shape))
    print("step 4 - done")
    #kovariacni matice C
    covArr = np.dot(arrayW, np.transpose(arrayW))
    #print(str(covArr.shape))
    #vlastni hodnoty a vektory
    eigVal, eigVec = np.linalg.eig(covArr)
    #print(str(np.argpartition(eigVal, 2)))
    #print(str(eigVal))
    sortIndices = np.argpartition(eigVal, 2)
    sortedEig = np.array([eigVec[sortIndices[0],:], eigVec[sortIndices[1],:], eigVec[sortIndices[2],:]])
    print("step 5 - done")
    #step 5 je v prednasce asi 7
    #vlastni prostor E
    EArr = np.transpose(np.dot(np.transpose(arrayW), sortedEig))
    #print(str(EArr.shape))
    print("step 6 - done")
    k1 = EArr[0,:]+avgArr
    k1res = np.transpose(np.reshape(k1, (width, height)))
    k2 = EArr[1,:]+avgArr
    k2res = np.transpose(np.reshape(k2, (width, height)))
    k3 = EArr[2,:]+avgArr
    k3res = np.transpose(np.reshape(k3, (width, height)))
    print("PCA done")
    return (k1res,k2res,k3res)

def get_hist(img):
    histogram=cv2.calcHist([img], [0], None, [256], [0,256])
    #print(str(histogram))
    return histogram

if __name__ == "__main__":
    img = loadImage("Cv09_obr.bmp")
    (k1,k2,k3)=PCA(img)
    #vykreslovani
    plt.subplot(2,4,1)
    gs = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    plt.imshow(gs, cmap="gray")
    plt.subplot(2,4,2)
    plt.imshow(k1, cmap="gray")
    plt.subplot(2,4,3)
    plt.imshow(k2, cmap="gray")
    plt.subplot(2,4,4)
    plt.imshow(k3, cmap="gray")
    #histogramy
    plt.subplot(2,4,5)
    hist=get_hist(gs)
    plt.plot(hist)
    plt.subplot(2,4,6)
    hist=get_hist(np.float32(k1))
    plt.plot(hist)
    plt.subplot(2,4,7)
    hist=get_hist(np.float32(k2))
    plt.plot(hist)
    plt.subplot(2,4,8)
    hist=get_hist(np.float32(k3))
    plt.plot(hist)
    plt.show()
