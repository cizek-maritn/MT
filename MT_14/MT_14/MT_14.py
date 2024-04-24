
def loadData(fn):
    f=open(fn, "r")
    return f.read().lower()

def indexKoincidence(text):
    N=len(text)
    temp=N*(N-1)
    IK=0
    for i in range(26):
        p=0
        current=97+i
        for j in range(N):
            if ord(text[j])==current:
                p+=1
        IK+=(p*(p-1))/temp
    print("IK: "+str(IK))
    if IK>0.063:
        print("anglictina")
        return 1
    else:
        print("cestina")
        return 2

def decode(lang, text):
    if lang==1:
        alphabet="eariotnslcudpmhgbfywkvxzjq"
    elif lang==2:
        pass
    alphDict={}
    for i in range(len(text)):
        current=text[i]
        if current in alphDict:
            alphDict[current]+=1
        else:
            alphDict.update({current: 1})
    print(str(alphDict))

if __name__=="__main__":
    text = loadData("cv14_text02.txt")
    print("vstup: "+text)
    lang=indexKoincidence(text)
    decode(lang,text)
