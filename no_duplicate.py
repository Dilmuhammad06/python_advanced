def copyright(n):
    
    haved = []

    into = []
    stro = []

    
    for i in range(0,len(n)):
        if n[i] not in haved:
            haved.append(n[i])
        else:
            haved.append('_')
    

    for i in range(1,5):
        for i in haved:
            if type(i) == int:
                into.append(i)
                haved.remove(i)
                

    # Sorting start
    for i in range(0,len(into)):
        value = into[i]

        while into[i-1] > value and i > 0:
            into[i],into[i-1] = into[i-1],into[i]
            i = i-1
    sorted_n = into
    # Soring end

    for i in haved:
        sorted_n.append(i)

    print(sorted_n)

        



copyright([1,2,4,3,0,2,0,2,3,5,4,6])