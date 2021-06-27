import string
def is_English(x):
    cnt = 0
    for ch in x:
        if ch in string.ascii_uppercase or ch in string.ascii_lowercase:
            cnt+=1
    if cnt/len(x)>0.5:
        return True
    return False
  
def is_Hindi_and_marathi(x):
    cnt = 0
    for char in x:
        if ord(u'\u0900') <= ord(char) <= ord(u'\u097F'):
            cnt+=1
    if cnt/len(x)>0.5:
        return True
    return False
  
def is_Punjabi(x):
    cnt=0
    for ch in x:
        if ord(ch) in range(2560, 2688):
            cnt+=1
    if cnt/len(x)>0.5:
        return True
    return False
  
def detect_language(x):
    if is_English(x):
        return 'English'
    elif is_Hindi_and_marathi(x):
        return 'Hindi+Marathi'
    elif is_Punjabi(x):
        return 'Punjabi'
    else:
        return 'Others'
      
def lang_decode(x):
    if x==101:
        return 'Punjabi'
    elif x==102:
        return 'English'
    elif x==103:
        return 'Hindi'
    elif x==104:
        return 'Marathi'
