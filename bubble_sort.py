def bubble_sort(mylist):
    len_index = len(mylist) - 1
    cc = 0
    sorter = False

    while not sorter:
        sorter = True

        for i in range(0, len_index):
            cc += 1
            if mylist[i] > mylist[i + 1]:
                sorter = False
                mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]

    return mylist, cc


print(bubble_sort([10, 2, 4, 12, 8, 11]))
