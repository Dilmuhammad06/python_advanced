def lost_num(n):
    cc = 0

    sorted_n = sorted(n)
    for i in range(0,max(sorted_n)):
        if i not in sorted_n:
            print(i)
        if i in sorted_n:
            cc+=1
            if cc == max(sorted_n):
                print(max(sorted_n)+1)





lost_num([3,2,1,0,4])