def difference(s,t):


    difference = ''


    for i in range(max(len(s), len(t))):
        if i < len(s) and i < len(t):
            if s[i] != t[i]:
                difference += t[i]
        else:
            difference += t[i:]

    print(difference)


difference('aa','aaa')