from binascii import a2b_base64
import numpy as np
import matplotlib.pyplot as plt
import struct
with open('cv01_dobryden.wav', 'rb') as f:
    #head
    data = f.read(4)
    print(data)
    A1 = struct.unpack('i', f.read(4))[0]
    print("bytu do konce souboru "+str(A1))
    w = f.read(8)
    print(w)
    AF = struct.unpack('i', f.read(4))[0]
    print("bytu do konce formatu "+str(AF))
    K = struct.unpack('h', f.read(2))[0]
    print("format komprese "+str(K))
    C = struct.unpack('h', f.read(2))[0]
    print("pocet kanalu "+str(C))
    VF = struct.unpack('i', f.read(4))[0]
    print("vzorkovaci frekvence " + str(VF))
    PB = struct.unpack('i', f.read(4))[0]
    print("prumerne bytu za sekundu "+str(PB))
    VB = struct.unpack('h', f.read(2))[0]
    print("velikost bloku vzorku "+str(VB))
    VV = struct.unpack('h', f.read(2))[0]
    print("velikost vzorku "+str(VV))
    d=f.read(4)
    print(d)
    A2 = struct.unpack('i', f.read(4))[0]
    print("pocet bytu do konce souboru "+str(A2))
    #data
    SIG=np.zeros(A2)
    for i in range(0,A2):
        SIG[i]=struct.unpack('B', f.read(1))[0]
t=np.arange(A2).astype(float)/VF
plt.plot(t, SIG)
plt.xlabel('t[s]')
plt.ylabel('A[-]')
plt.show()
