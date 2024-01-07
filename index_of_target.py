def indexer(n,t):
    cc = -1
    ccc = -1
    
    inn = bool

    for i in n:
        cc+=1
        if i == t:
            print(f'Here an index: {cc}')
        else:
            inn = False
            n.append(t)
        break

    if inn == False:
            sorted_n = sorted(n)
            for i in sorted_n:
                 ccc+=1
                 if i == t:
                      sorted_n.remove(t)
                      print(sorted_n)
                      print(f'Needed index: {ccc}')


indexer([1,3,5,6],7)