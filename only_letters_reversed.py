def string_reverser(word):
    letters_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']
    letters_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    worldo = []

    for i in word:
        if i in letters_low or i in letters_up:
            worldo.append(i)
    aa = worldo[::-1]
    res = ''.join(aa)
    print(res)

string_reverser('H-el/l_o Wo_r\ld')