listone = [11]
listsec = [222]
freelisto = []


def listo_add(one, two):
    for i in one:
        for q in two:
            c = i + q
            c = int(c)
            print(c)


listo_add(listone, listsec)
