def bubble_sort(mylist):
    len_index = len(mylist) - 1
    sorter = False

    while not sorter:
        sorter = True

        for i in range(0, len_index):
            if mylist[i] > mylist[i + 1]:
                sorter = False
                mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]

    return mylist[::-1]


print(bubble_sort([10, 2, 4, 12, 8, 11]))
