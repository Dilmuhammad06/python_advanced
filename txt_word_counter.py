def Tom_Riddle_The_Reader():
    cc=0
    with open('testo.txt','r') as rd:
        reader = rd.read()
        a = reader.split()
        lenght = len(a)
    return f'Sozlar: {lenght}'
print(Tom_Riddle_The_Reader())