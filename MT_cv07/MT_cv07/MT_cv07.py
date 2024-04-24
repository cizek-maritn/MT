import struct
import os

def loadData(filename):
    f=open(filename, "rb")
    output=""
    for i in range(os.path.getsize(filename)):
        temp=struct.unpack("B", f.read(1))[0]
        output=output+str(temp)
    return output

def aritComp(data):
    size=len(data)
    print("vstupni data: "+data)
    #vytvareni intervalu, delam ho fixne a ne dynamicky
    prob={"1": 0,
          "2": 0,
          "3": 0,
          "4": 0}
    for i in range(size):
        prob[str(data[i])]+=1

    for i in prob:
        prob[i]=prob[i]/size
        try:
            #z nejakyho bohovi neznameho duvodu mi vychazelo 0.60000000001
            prob[i]=round(prob[i]+val,2)
        except:
            pass
        val=prob[i]
    
    #kodovani
    #pouziju list pro interval
    interval=[0,1]
    for i in range(size):
        current=data[i]
        cHigh=prob[current]
        #cLow muze byt 0, ktera v prob dictionairy neni
        try:
            cLow=prob[str(int(current)-1)]
        except:
            cLow=0

        #uprava intervalu
        newLow=interval[0]+(cLow*(interval[1]-interval[0]))
        newHigh=interval[0]+(cHigh*(interval[1]-interval[0]))
        interval[0]=newLow
        interval[1]=newHigh
    
    #vytvareni vysledne hodnoty, kde se hodnoty meni, vezmu tu vetsi a zbytek zahodim
    strLow=str(interval[0])
    strHigh=str(interval[1])
    final=""
    for i in range(len(strHigh)):
        if strHigh[i]==strLow[i]:
            final+=strHigh[i]
        else:
            final+=strHigh[i]
            break
    print("vysledek komprese: "+final)
    output=float(final)

    return prob, output, size

def aritDecomp(prob, value, size):
    interval=[0,1]
    output=""
    for i in range(size):
        result=((value-interval[0])/(interval[1]-interval[0]))
        for j in prob:
            if result<prob[j]:
                output+=str(j)
                current=str(j)
                break
        #prakticky ctrl+c, ctrl+v
        cHigh=prob[current]
        try:
            cLow=prob[str(int(current)-1)]
        except:
            cLow=0
        newLow=interval[0]+(cLow*(interval[1]-interval[0]))
        newHigh=interval[0]+(cHigh*(interval[1]-interval[0]))
        interval[0]=newLow
        interval[1]=newHigh

    print("vysledek dekomprese: "+output)

if __name__ == "__main__":
    data=loadData("Cv07_Aritm_data.bin")
    prob, comp, size=aritComp(data)
    aritDecomp(prob, comp, size)
