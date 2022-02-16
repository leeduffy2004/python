uniquewords=[]

def findUnique(word):
    for w in uniquewords:
        if w==word:
            return False
    
    uniquewords.append(word)
    return True

def removedduplicates(msg):
    newmsg=""
    word=""
    i=0
    while i<len(msg):
        if msg[i]==" ":
            if findUnique(word):
                newmsg=newmsg+word+" "
            word=""
        else:
            word=word+msg[i]
        i=i+1
    if findUnique(word):
        newmsg=newmsg+word
    print(newmsg)

removedduplicates("hello hello hello yes yes please please thank thank you you")


