import re

text = '''Albert Einstein (/ˈaɪnstaɪn/ EYEN-styne;[4] German:                                        
[ˈalbɛɐt ˈʔaɪnʃtaɪn ⓘ; 14 March 1879 – 18 April 1955) was a                                         
German-born theoretical physicist who is widely held to be one of the greatest                       
 and most influential scientists of a ll )time. Best} known for developing the theory of relativity,    
  Einstein also made important(() contributions to quantum mechanics, and was thus a central figure'''

def find_char_indexes():
    finders = ['a', 'A']

    for finder in finders:
        location = -1
        for i, char in enumerate(text):
            if char == finder:
                location = i
                print(f'{finder} has been found at index = {location}')
                break  # Stop the loop when the character is found

find_char_indexes()
