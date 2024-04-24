def inverseCode(a,b):
    print("hodnoty: "+str(a)+" "+str(b))
    binA = bin(a)[2:]
    binB = bin(b)[2:]
    #doplnuju leading nuly
    if len(binA)>len(binB):
        diff=len(binA)-len(binB)
        binB=("0"*diff)+binB
    if len(binA)<len(binB):
        diff=len(binB)-len(binA)
        binA=("0"*diff)+binA
    #kontrolni soucet
    zeros=0
    inverted=0
    for i in range(len(binA)):
        if binA[i]=="0":
            zeros+=1
    if zeros%2==1:
        inverted=1
        newBinB=""
        for i in range(len(binB)):
            if binB[i]=="0":
                newBinB+="1"
            else:
                newBinB+="0"
        binB=newBinB
    conSum=bin(int(binA,2)+int(binB,2))[2:]
    if len(conSum) > max(len(binA), len(binB)):
        conSum=conSum[1:]
    #zjistovani typu chyby
    ones=0
    index0 = 0
    index1= 0
    for n in range(len(conSum)):
        if conSum[n]=="1":
            ones+=1
            index1=n
        else:
            index0=n
    #oprava chyby
    print(binA)
    print(binB)
    print(conSum)
    if ones==1:
        print("chyba zab. casti kodu na pozici: " + str(index1))
        if inverted==1:
            #if binB[index1]=="0":
            #    change="1"
            #else:
            #    change="0"
            #binB=binB[:index1]+change+binB[index1+1:]
            print("opravena binaraka: "+binA)
            print("spravne cislo: "+str(int(binA,2)))
        else:
            if binA[index1]=="0":
                change="1"
            else:
                change="0"
            binA=binA[:index1]+change+binA[index1+1:]
            print("opravena binarka: "+binA)
            print("spravne cislo: "+str(int(binA,2)))
    else:
        print("chyba infor. casti kodu na pozici: " + str(index0))
        if binA[index0]=="0":
            change="1"
        else:
            change="0"
        binA=binA[:index0]+change+binA[index0+1:]
        print("opravena binarka: "+binA)
        print("spravne cislo: "+str(int(binA,2)))

if __name__ == "__main__":
    inverseCode(160, 223)
    inverseCode(64,65)
    inverseCode(128,126)
