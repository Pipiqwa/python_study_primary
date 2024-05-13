while True:
    try:
        str1 = input()
        str2 = str1[2:]
        n = len(str2)
        dic = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        x1 = 0
        for word in str2:
            if word in dic:
                x1 = x1 + dic[word]*16**(n-1)
                n = n - 1
            else:
                x1 = x1 + int(word)*16**(n-1)
                n = n - 1
        print(x1)

    except:
        break