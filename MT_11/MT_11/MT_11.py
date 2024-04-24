def grayCode():
    print("dec\tbin\t\tgray")
    for i in range(256):
        binNum = bin(i)
        binNum=binNum[2:]
        temp=binNum[0]
        output=temp
        for n in range(len(binNum)-1):
            xor = int(temp)^int(binNum[n+1])
            output+=(str(xor))
            temp=binNum[n+1]
        print(str(i)+"\t"+binNum+"\t\t"+output)

def moveToFront():
    word=input("zadej slovo\n")
    word=word.upper()
    #abeceda
    alph=[]
    decodeAlph=[]
    for i in range(26):
        alph.append(chr(65+i))
        decodeAlph.append(chr(65+i))
    #print(str(alph))
    output=""
    for i in word:
        temp=alph.index(i)
        output+=str(temp+1)+","
        #print(output)
        alph.insert(0, alph.pop(temp))
    output=output[:-1]
    print("input: "+word+"\toutput: "+output)
    #dekodovani
    info=output.split(",")
    decodeOut=""
    for item in info:
        decodeOut+=decodeAlph[int(item)-1]
        decodeAlph.insert(0, decodeAlph.pop(int(item)-1))
    print("input: "+output+"\toutput: "+decodeOut)

def BWT():
    word=input("zadej slovo\n")
    word=word.upper()
    wordList=[]
    output=""
    for i in range(len(word)):
        wordList.append(word)
        word=word[-1]+word[:-1]
    wordList=sorted(wordList)
    for i in wordList:
        output+=i[-1]
    output+=","+str(wordList.index(word)+1)
    print("zakodovano: "+output)
    #print(str(wordList))
    #dekodovani
    length=len(output[:-2])
    arr = [["a" for i in range(length)] for j in range(length)]
    #pocatecni stav
    for i in range(length):
        arr[i][0]=output[i]
    #zbytek
    for i in range(length-1):
        #vezme sloupec
        tempList = [row[i] for row in arr]
        tempList=sorted(tempList)
        for j in range(length):
            arr[j][i+1]=arr[j][i]+tempList[j][-1]
        #print(str(tempList))
    #print(str(arr))
    decodeList=[row[length-1] for row in arr]
    decodeList=sorted(decodeList)
    print("dekodovano: "+decodeList[int(output.split(",")[1])-1])

if __name__ == "__main__":
    grayCode()
    moveToFront()
    BWT()
