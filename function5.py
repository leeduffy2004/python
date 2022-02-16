def wordcount(msg):
    space=0
    i=0
    while i<len(msg):
        if msg[i]==" ":
            space=space+1
        i=i+1

    print("In the message we found:",space+1)

wordcount("Hello my Friends")
wordcount("My favourite team is Manchester United")
wordcount("David Beckham played for Manchester United and England")