def rep(listo):
    letters = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
        'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }
    lister = []
    for i in listo:
        for j in i:
            for s in j:
                if s in letters:
                    letters[s]+=1
    for key,value in letters.items():
        if value > 1:
            print(f'{key} = {value}')
            lister.append(key)
    print(lister)

rep(['hello','wassup','whatsapp'])