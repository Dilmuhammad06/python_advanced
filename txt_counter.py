def counnter_txt():
    with open('test.txt', 'r') as a:
        reader = a.read()

    cc = len(reader.split())
    print(f"The number of words in txt text: {cc}")


counnter_txt()