def selection(listo):
    for i in range(len(listo)):
        min_index = i

        for j in range(i + 1, len(listo)):
            if listo[j] < listo[min_index]:
                min_index = j

        listo[i], listo[min_index] = listo[min_index], listo[i]

    return listo

print(selection([8, 2, 5, 11, 22, 18]))
