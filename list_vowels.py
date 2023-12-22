def list_count(listo):
    cc=0
    cv=0
    leno = len(listo)

    for i in (0,leno):
        pass
    for o in listo:
        for j in o:
            if j.upper() in ['A', 'E', 'I', 'O', 'U']:
                cv+=1

    return f' Sozlar: {i}, Unlilar: {cv}'



print(list_count(['Hello','World','Man']))