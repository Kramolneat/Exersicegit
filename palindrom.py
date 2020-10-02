text = 'mofvbnm,m'
for i in range (0,len(text)):
    if i < len(text)/2:
        if text[i] == text[len(text)-i-1]:
            print('palindorm')
        else:
            print('not')
        
        
