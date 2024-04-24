#burrow wheeler, movetofirst, aritmeticke kodovani, lzw, Huffman
import numpy as np
import math
import random

def primeNumberGen(lowNum, highNum):
    highNum+=1
    primeNumbers=[]
    arr=np.ones(highNum, dtype=bool)
    for i in range(int(math.sqrt(highNum))):
        if arr[i+2]==True:
            j=(i+2)*(i+2)
            while j<highNum:
                arr[j]=False
                j+=(i+2)
    for i in range(highNum):
        if i<lowNum:
            pass
        elif arr[i]==True:
            primeNumbers.append(i)
    return random.sample(primeNumbers,2)

def rsa(p,q):
    data=input("input data: ")
    dataList = list(data)
    for i in range(len(dataList)):
        dataList[i]=ord(dataList[i])
    #print(str(dataList))
    #modul
    n=p*q
    #Eulerova funkce
    EulFun=(p-1)*(q-1)
    #nahodny vyber, mensi jak EulFun
    e=random.randint(2,EulFun-1)

    while math.gcd(e, EulFun) != 1:
        e = random.randint(2, EulFun - 1)
    #d=random.randint(2,EulFun-1)
    #attempt=1
    #while not ((e*d)%EulFun==1):
    #    attempt=1
    #    while attempt<80000:
    #        d=random.randint(2,EulFun-1)
    #        attempt+=1
    #    e=random.randint(2,EulFun-1)
    #    print("again")
    d=pow(e,-1,EulFun)
    print("moving on")
    #print(str(e)+" "+str(d)+" "+str(EulFun))
    encrypted=[]
    for i in dataList:
        encrypted.append(pow(i,e,n))
    decrypted=[]
    for i in encrypted:
        decrypted.append(chr(pow(i,d,n)))
    print("vstupni data: "+data)
    print("modulo: "+str(n))
    print("EulFun: "+str(EulFun))
    print("e a d: "+str(e)+" "+str(d))
    print("zasifrovano: "+str(encrypted))
    print("desifrovano: "+str(decrypted))

if __name__ == "__main__":
    (p,q)=primeNumberGen(1000, 10000)
    rsa(p,q)
    #print(str(p)+" "+str(q))

