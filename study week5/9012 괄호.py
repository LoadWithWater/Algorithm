T = int(input())

stringline = ''

for i in range(T):
    stringline = str(input())
    stringline = list(stringline)

    if (stringline[0] == "(" and stringline[-1] == ")"):
        leftcount = 0
        rightcount = 0
        for j in range(len(stringline)):    
            if (stringline[j] == "("):
                leftcount += 1
            else:
                rightcount += 1
        if (leftcount == rightcount):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")







