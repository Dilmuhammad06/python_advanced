listo = [789,753,123,1,8]
sorted_list = []
def sorter():
    for i in range(1,1000):
        for l in listo:
            if i == l:
                sorted_list.append(l)
    print(sorted_list)
sorter()