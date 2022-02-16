def printing(msg):
    word=""
    i=len(msg)-1

    while i>=0:
        if msg[i]==" ":
            print(word)
            word=""
        else:
            word=msg[i]+word
        i=i-1
    print(word)

printing("Welcome to the Jungle")
printing("How you doing")
printing("Jungle the to Welcome")
printing("doing you How")