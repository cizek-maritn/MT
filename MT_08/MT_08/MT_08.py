import cv2
import numpy as np
import matplotlib.pyplot as plt
import struct

if __name__ =="__main__":
    cap = cv2.VideoCapture('cv08_video.mp4')
    NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    redx1 = np.array([208, 209,210,211])
    redx2 = np.array([268,269,270,271])
    #prvni krok zvlast
    oldret, oldbgr = cap.read()
    oldrgb = cv2.cvtColor(oldbgr, cv2.COLOR_BGR2RGB)
    oldgs = cv2.cvtColor(oldbgr, cv2.COLOR_BGR2GRAY)
    oldhist=cv2.calcHist([oldgs], [0], None, [256], [0,256])
    imf=np.float32(oldgs/255.0)
    olddct=cv2.dct(imf)
    #print(str(olddct))
    oldsuma=0
    h, w = oldrgb.shape[:2]
    dcth, dctw = olddct.shape[:2]
    for x in range(w):
        for y in range(h):
            red=int(oldrgb[y][x][0])
            green=int(oldrgb[y][x][1])
            blue=int(oldrgb[y][x][2])
            oldrgbval=int(red+blue+green)
            oldsuma+=oldrgbval
    #listy pro vykresleni
    firstList=[0]
    secondList=[0]
    thirdList=[0]
    fourthList=[0]
    #zbytek videa
    for i in range(1, NFrames):
        print(str(i) + " of " + str(NFrames))
        ret, bgr = cap.read()
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        gs = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        hist=cv2.calcHist([gs], [0], None, [256], [0,256])
        imf=np.float32(gs/255.0)
        dct=cv2.dct(imf)
        #histsuma a dctsuma jsou celkem self explanatory
        histsuma=0
        dctsuma=0
        for j in range(256):
            histsuma+=int(abs(oldhist[j]-hist[j]))
            #print(str(histsuma))
        for x in range(dctw):
            for y in range(dcth):
                dctsuma+=float(abs(olddct[y][x]-dct[y][x]))
        #suma je pro prvni metodu a suma2 pro druhou - jsem si plne vedom jak hnusne to je napsany
        suma=0
        suma2=0
        for x in range(w):
            for y in range(h):
                red=int(rgb[y][x][0])
                green=int(rgb[y][x][1])
                blue=int(rgb[y][x][2])
                oldred=int(oldrgb[y][x][0])
                oldgreen=int(oldrgb[y][x][1])
                oldblue=int(oldrgb[y][x][2])
                rgbval=int(red+green+blue)
                oldrgbval=int(oldred+oldgreen+oldblue)
                suma+=rgbval
                suma2+=abs(oldrgbval-rgbval)
        diff=abs(oldsuma-suma)
        firstList.append(diff)
        secondList.append(suma2)
        thirdList.append(histsuma)
        fourthList.append(dctsuma)
        oldsuma=suma
        oldrgbval=rgbval
        oldrgb=rgb
        oldhist=hist
        olddct=dct
    #vykreslovani
    plt.subplot(2,2,1)
    #maxVal a redy jsou hodnoty pro vykreslovani cervenych "zlomu" v grafech na mistech 209-210 a 269-270
    maxVal = max(firstList)
    redy = np.array([0, maxVal, maxVal, 0])
    plt.plot(redx1, redy, color = 'r')
    plt.plot(redx2, redy, color = 'r')
    plt.plot(firstList, color = 'b')
    plt.subplot(2,2,2)
    maxVal = max(secondList)
    redy = np.array([0, maxVal, maxVal, 0])
    plt.plot(redx1, redy, color = 'r')
    plt.plot(redx2, redy, color = 'r')
    plt.plot(secondList, color = 'b')
    plt.subplot(2,2,3)
    maxVal = max(thirdList)
    redy = np.array([0, maxVal, maxVal, 0])
    plt.plot(redx1, redy, color = 'r')
    plt.plot(redx2, redy, color = 'r')
    plt.plot(thirdList, color = 'b')
    plt.subplot(2,2,4)
    maxVal = max(fourthList)
    redy = np.array([0, maxVal, maxVal, 0])
    plt.plot(redx1, redy, color = 'r')
    plt.plot(redx2, redy, color = 'r')
    plt.plot(fourthList, color = 'b')
    plt.show()

    #prehravani videa
    cap = cv2.VideoCapture('cv08_video.mp4')
    figure = plt.figure()
    NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    maxVal = max(firstList)
    redy = np.array([0, maxVal, maxVal, 0])
    for i in range(1, NFrames):
        ret, bgr = cap.read()
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        figure.clear()
        plt.imshow(rgb, aspect='auto', extent = [0, 304, min(firstList), max(firstList)])
        plt.plot(redx1, redy, color = 'r')
        plt.plot(redx2, redy, color = 'r')
        plt.plot(firstList, color = 'b')
        l = plt.axvline(x=i, color='g')
        plt.axis([0, 304, min(firstList), max(firstList)])
        plt.show(block=False)
        plt.pause(0.001)
