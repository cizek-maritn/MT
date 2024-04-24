from binascii import a2b_base64
import numpy as np
import matplotlib.pyplot as plt
import struct

with open('cv02_wav_04.wav', 'rb') as f:
    #chceme string RIFF
    data=f.read(4).decode()
    if data!="RIFF":
        raise Exception("nejedna se o RIFF soubor " + str(data))
    #pocet bytu do konce souboru
    A1 = struct.unpack('i', f.read(4))[0]
    #chceme string WAVEfmt_
    w=f.read(8).decode()
    if w!="WAVEfmt ":
        raise Exception("nejedna se o WAVE soubor " + str(w))
    #pocet bytu do konce formatu, min 16B
    AF = struct.unpack('i', f.read(4))[0]
    if AF<16:
        raise Exception("cast format je moc mala " + str(AF))
    #komprese
    K = struct.unpack('h', f.read(2))[0]
    if K!=1:
        raise Exception("spatna komprese " + str(K))
    #pocet kanalu
    C = struct.unpack('h', f.read(2))[0]
    #vzorkovaci frekvence
    VF = struct.unpack('i', f.read(4))[0]
    #prumerny pocet bytu za sekundu
    PB = struct.unpack('i', f.read(4))[0]
    #velikost bloku
    VB = struct.unpack('h', f.read(2))[0]
    #velikost vzorku
    VV = struct.unpack('h', f.read(2))[0]
    if VB!=VV*C/8:
        raise Exception("nevysel kontrolni vypocet velikosti bloku " + str(VB) + " " + str(VV*C/8))
    if PB!=VF*VB:
        raise Exception("nevysel kontrolni vypocet prumerneho poctu bytu" + str(PB) + " " + str(VF*VB))
    #chceme string data
    d=f.read(4).decode()
    if d!="data":
        raise Exception("vzorec data je spatne")
    #pocet bytu do konce souboru
    A2=struct.unpack('i', f.read(4))[0]
    if A1!=(A2+20+AF):
        raise Exception("nevysel kontrolni vypocet delky souboru " + str(A1) + " " + str(A2) + " " + str(A2+20+AF))
    #data
    #pocet radku pro vykres signalu
    pr=round(C/2)
    print("pocet radku: " + str(pr))
    print(str(C))
    print(str(VB))
    SIG=[[0 for i in range(int(A2/VB))] for j in range(C)]
    #jak velky kus dat ma projit unpackem
    if VB/C==1:
        rs='B'
    else:
        rs='h'

    for i in range(0,int(A2/VB)):
        for j in range(0,C):
            SIG[j][i]=struct.unpack(rs, f.read(int(VB/C)))[0]


t=np.arange(int(A2/VB)).astype(float)/VF
if C>1:
    for i in range(0,C):
        plt.subplot(pr, 2, i+1)
        plt.plot(t, SIG[i][::])
        plt.title("kanal " + str(i+1))
        plt.xlabel('t[s]')
        plt.ylabel('A[-]')
else:
    plt.plot(t, SIG[0][::])
    plt.title("kanal 1")
    plt.xlabel('t[s]')
    plt.ylabel('A[-]')
plt.show()
