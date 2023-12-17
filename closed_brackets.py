import re

text = '''Albert Einstein (/ˈaɪnstaɪn/ EYEN-styne;[4] German:                                        
[ˈalbɛɐt ˈʔaɪnʃtaɪn ⓘ; 14 March 1879 – 18 April 1955) was a                                         
German-born theoretical physicist who is widely held to be one of the greatest                       
 and most influential scientists of a ll )time. Best} known for developing the theory of relativity,    
  Einstein also made important(() contributions to quantum mechanics, and was thus a central figure'''

def brackets_c(a=text):
    cir_br_open = re.findall(r'[(]', a)
    cir_br_close = re.findall(r'[)]', a)

    cam_br_open = re.findall(r'[{]', a)
    cam_br_close = re.findall(r'[}]', a)

    list_br_open = re.findall(r'[\[]', a)
    list_br_close = re.findall(r'[\]]', a)

    cir_open = len(cir_br_open)
    cir_close = len(cir_br_close)
    cam_open = len(cam_br_open)
    cam_close = len(cam_br_close)
    list_open = len(list_br_open)
    list_close = len(list_br_close)

    if cir_open == cir_close:
        print('( ) berkitilgan')
    else:
        print(f'( ) {max(cir_open, cir_close)} ta berkitilmagan')

    if cam_open == cam_close:
        print('{ } berkitilgan')
    else:
        print(f'{ { }} {max(cam_open, cam_close)} ta berkitilmagan')

    if list_open == list_close:
        print('[ ] berkitilgan')
    else:
        print(f'[ ] {max(list_open, list_close)} ta berkitilmagan')

brackets_c()
