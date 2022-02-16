def printing(msg):
    word=""
    i=0

    while i<len(msg):
        if msg[i]==" ":
            print(word)
            word=""
        else:
            word=word+msg[i]
        i=i+1
    print(word)

printing("Welcome to the Jungle")
printing("How you doing")