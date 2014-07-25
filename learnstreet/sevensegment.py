def  illuminate(num):
    "REPLACE THIS CODE WITH YOUR illuminate() METHOD"
    if num ==1:
        return 'nyynnnn'
    elif num == 2:
        return 'yynyyny'
    elif num == 3:
        return 'yyyynny'
    elif num == 4:
        return 'nyynnyy'
    elif num ==5:
        return 'ynyynyy'
    elif num ==6:
        return 'ynyyyyy'
    elif num ==7:
        return 'yyynnnn'
    elif num == 8:
        return 'yyyyyyy'
    elif num ==9:
        return 'yyyynyy'
    else:
        return 'yyyyyyn'
    
def  get_digits(text):
    "REPLACE THIS CODE WITH YOUR getDigits() METHOD"
    s = ('1','2','3','4','5','6','7','8','9','0')
    l = []
    for char in text:
        #print char,s
        if char in s:
            #print char
            l.append(char)
    print l
    return l

def main():
    get_digits('thi9sd920 4jds')
if __name__=='__main__':
    main()