import struct
import os
import operator

def loadData(filename):
    f=open(filename, "rb")
    output=""
    for i in range(os.path.getsize(filename)):
        temp=struct.unpack("B", f.read(1))[0]
        output=output+str(temp)
    return output

#RLE komprese, vystup ve formatu "<pocet> <znak>", oddeleno lomitkem
def rleComp(data):
    count=0
    output=""
    current=data[0]
    #prochazeni dat
    for i in range(len(data)):
        if data[i]==current:
            count+=1
        else:
            output+=str(count)+" "+str(current)+" / "
            current=data[i]
            count=1
    #posledni krok musim udelat zvlast
    output+=str(count)+" "+str(current)
    current=data[i]
    count=1
    print("vstupni data: "+data)
    print("vystup komprese: "+output)
    return output

def rleDecomp(data):
    output=""
    cells=data.split("/")
    #prochazeni kodovanych dat
    for i in range(len(cells)):
        #count je pocet vyskytu, num je znak
        count=int(cells[i].split()[0])
        num=cells[i].split()[1]
        for i in range(count):
            output+=num
    print("vystup dekomprese: "+output)

def huffComp(data):
    alphabet = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0
    }
    print("vstupni data: " + data)
    origRange=len(alphabet)
    #ziskavani cetnosti
    for i in range(len(data)):
        alphabet[str(data[i])]+=1
    #print(str(alphabet))
    #vytvareni "tabulky"
    table={}
    
    for i in range(origRange):
        max_key=max(alphabet, key=alphabet.get)
        max_val=max(alphabet.values())
        table.update({max_key:round(max_val/len(data),2)})
        alphabet.pop(max_key)
    #print(str(table))
    #vytvareni klicu
    finalAlphabet={
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": ""
    }
    for i in range(origRange-1):
        lowest_key=min(table, key=table.get)
        lowest_val=min(table.values())
        for j in range(len(lowest_key)):
            finalAlphabet[lowest_key[j]]="0"+finalAlphabet[lowest_key[j]]
        table.pop(lowest_key)
        lowest_key2=min(table, key=table.get)
        lowest_val2=min(table.values())
        for j in range(len(lowest_key2)):
            finalAlphabet[lowest_key2[j]]="1"+finalAlphabet[lowest_key2[j]]
        table.pop(lowest_key2)
        table.update({(lowest_key2+lowest_key):lowest_val+lowest_val2})
    print("konecna tabulka: "+str(finalAlphabet))

    #komprese dat
    output=""
    for i in range(len(data)):
        output+=finalAlphabet[data[i]]+" " 
    print("komprese dat: "+output)

    #dekomprese dat
    decompData=output.split()
    decompOutput=""
    #inverze abecedy pro jednodussi praci
    invAlphabet={v: k for k, v in finalAlphabet.items()}
    for i in range(len(decompData)):
        decompOutput+=invAlphabet[decompData[i]]
    print("dekomprese dat: "+decompOutput)


if __name__ == "__main__":
    huffFile="Cv05_LZW_data.bin"
    rleFile="Cv06_RLE_data.bin"
    #RLE kodovani
    print("RLE komprese")
    rleData=loadData(rleFile)
    rleCompressed=rleComp(rleData)
    rleDecomp(rleCompressed)
    #Huffmanovo kodovani
    print("Huffmanova komprese")
    huffData=loadData(huffFile)
    huffComp(huffData)
    
