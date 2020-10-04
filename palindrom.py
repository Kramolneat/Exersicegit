import sys
text = sys.argv[1]
ispalindrom = True
for i in range (0,len(text)/2):
    if text[i] != text[len(text)-i-1]:
        ispalindrom = False
        break

print(text+' is'+('' if ispalindrom else ' not')+' palindrom')
