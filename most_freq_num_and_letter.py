import re
from collections import Counter

text = '''Albert Einstein (/ˈaɪnstaɪn/ EYEN-styne;[4] German: 
[ˈalbɛɐt ˈʔaɪnʃtaɪn] ⓘ; 14 March 1879 – 18 April 1955) was a 
German-born theoretical physicist who is widely held to be one of the greatest
 and most influential scientists of all time. Best known for developing the theory of relativity,
  Einstein also made important contributions to quantum mechanics, and was thus a central figure'''
def matn():
    letters_numbers = re.findall(r'[A-Za-z0-9]', text)
    counter = Counter(letters_numbers)

    most = counter.most_common(2)

    if most:
        lettero, letterest = most[0]
        num_counter = Counter(re.findall(r'\d', text))
        most_common_number = num_counter.most_common(1)

        if most_common_number:
            num, numberst = most_common_number[0]
            print(f"Freq letter: {lettero}, Freq num: {num}")


matn()