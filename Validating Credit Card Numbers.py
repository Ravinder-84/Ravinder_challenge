import re 

pattern1 = r'[456]\d{3}\-?\d{4}\-?\d{4}\-?\d{4}'
pattern2 = r'(\d)\1{3,}'

for _ in range(int(input())):
    card_num = input()
 
    match = re.fullmatch(pattern1, card_num) 
    if match:
        repetition_check = re.search(pattern2, card_num.replace('-','')) 
        if repetition_check:
            print('Invalid')
        else:
            print('Valid') 
    else:
        print('Invalid') 