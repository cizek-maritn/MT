import struct
import os

#nacteni dat do stringu
def load_data(fname):
    f=open(fname, "rb")
    output=""
    for i in range(os.path.getsize(fname)):
        temp=struct.unpack("B", f.read(1))[0]
        output=output+str(temp)
    return output

#komprese
def compress(data):
    #jako abecedu pouziju list, list item je fraze, index v listu + 1 je index fraze
    alphabet=["1","2","3","4","5"]
    output=""
    #prochazeni do konce souboru
    while len(data)>=1:
        contains=1
        start=data[0]
        #print("test")
        try:
            #pokud list obsahuje frazi, projdu list znova s dalsim znakem navic, dokud novou frazi nenajdu
            iteration=1
            while contains==1:
                contains=0
                temp=start+data[iteration]
                #print(temp)
                #print(data[iteration])
                #print(str(iteration))
                #print("next")
                #print("test")
                for i in range(len(alphabet)):
                    #print(str(i))
                    if alphabet[i]==start:
                        candidate=i+1
                        #print("test")
                    if alphabet[i]==temp:
                        #print("test")
                        contains=1
                        iteration=iteration+1
                        start=temp
            output=output+str(candidate)+" "
            alphabet.append(temp)
            data=data[len(start):]
        except:
            for i in range(len(alphabet)):
                if alphabet[i]==start:
                    output=output+str(i+1)
                    data=""
    print("vysledek komprese: "+output)
    print("abeceda komprese: "+str(alphabet))
    return output

def decompress(data):
    data=data.split()
    alphabet=["1","2","3","4","5"]
    output=""
    previous=""
    current=""
    newPhrase=""
    #prvni krok
    for i in range(len(alphabet)):
        if data[0]==alphabet[i]:
            previous=alphabet[i]
            output=output+previous
    #zbytek
    for i in range(len(data)-1):
        num=int(data[i+1])
        if num>len(alphabet):
            newPhrase=previous+previous[0]
            output=output+newPhrase
            alphabet.append(newPhrase)
            #print("B")
        else:
            current=alphabet[num-1]
            output=output+current
            newPhrase=previous+current[0]
            alphabet.append(newPhrase)
            #print("A")
        previous=current
    print("vysledek dekomprese: " + output)
    print("abeceda dekomprese: " + str(alphabet))


if __name__ == "__main__":
    data=load_data("Cv05_LZW_data.bin")
    print("originalni data: " + data)

    #komprese
    comp_data=compress(data)
    #dekomprese
    decompress(comp_data)

