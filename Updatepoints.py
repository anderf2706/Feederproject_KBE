
def update(point):
    a= ''
    liste = []
    toMM = 500
    for i in point:

        if i.isdigit():
            a+= i
        else:
            if len(a) > 0:
                liste.append(a)
                a=''

    liste = list(map(int, liste))

    finalList =[]

    count= 1
    for i in liste:
        if count == 3:
            count= 1
        if count== 1:
            a= i
        elif count ==2:
            b= i
        if count== 2:
            finalList.append((a*toMM, b*toMM))

        count += 1

    return finalList

