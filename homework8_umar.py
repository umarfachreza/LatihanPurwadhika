# number 1
def getsquare(num) :
    num = str(num)
    square = ''
    for item in num :
        square += str(int(item)*int(item))
    return int(square)

print(getsquare(121))
print(getsquare(553))
print(getsquare(44991))

# number 2
listname = ["Ryan", "Kieran", "Jason", "Yous"] 
print(listname)

def filterfriends(list_name) : 
    friends = [item for item in list_name if len(item) == 4]
    return friends

print(filterfriends(listname))

#number 3

def countwords(kalimat) :
    a = kalimat.split(' ')
    b=len(a)
    return 'ada {} kata'.format(b)

print(countwords('budi pergi ke pasar ikan'))

#number 4
def smallenough(listangka,num) :
    sum1=0
    for item in listangka :
        sum1+=item
    print(sum1)
    if sum1>=num :
        print(False)
    else :
        print(True)

(smallenough([100,99,56,69,27,101,18],471))
print(sum([100,99,56,69,27,101,18]))

# number 5
def DomainName(domain) :
    listdomain=domain.split('.')
    if len(listdomain)==3 :
        print(listdomain[1])
    elif len(listdomain)==2 :
        print(listdomain[0].split('//')[1])

DomainName('http://github.com/carbonﬁve/raygun')
DomainName('http://www.zombie-bites.com')
DomainName('https://www.cnet.com')

#number 6
def wave(kata) :
    newlist=[]
    for i in range(len(kata)) :
        kata1=''
        for j in range(len(kata)) :
            if i == j :
                kata1+=kata[j].upper()
            else :
                kata1+=kata[j].lower()
        newlist.append(kata1)
    return newlist

print(wave('jakartA'))

#number 7
def removeduplikat(kalimat) :
    kalimat = kalimat.split(' ')   
    katakata = ''
    for item in kalimat :
        if not(item in katakata) :
            katakata += (item +' ')
    print(katakata)

removeduplikat('alpha beta beta beta gamma gamma')

#number 8
def stringy(angka) :
    number=''
    for i in range(angka) :
        if((i+1)%2==0) :
            number += '0'
        elif (i+1)%2==1 :
            number +='1'
    print(int(number))

stringy(12)
stringy(3)
# number 1
def getsquare(num) :
    num = str(num)
    square = ''
    for item in num :
        square += str(int(item)*int(item))
    return int(square)

print(getsquare(121))
print(getsquare(553))
print(getsquare(44991))

# number 2
listname = ["Ryan", "Kieran", "Jason", "Yous"] 
print(listname)

def filterfriends(list_name) : 
    friends = [item for item in list_name if len(item) == 4]
    return friends

print(filterfriends(listname))

#number 3

def countwords(kalimat) :
    a = kalimat.split(' ')
    b=len(a)
    return 'ada {} kata'.format(b)

print(countwords('budi pergi ke pasar ikan'))

#number 4
def smallenough(listangka,num) :
    sum1=0
    for item in listangka :
        sum1+=item
    print(sum1)
    if sum1>=num :
        print(False)
    else :
        print(True)

(smallenough([100,99,56,69,27,101,18],471))
print(sum([100,99,56,69,27,101,18]))

# number 5
def DomainName(domain) :
    listdomain=domain.split('.')
    if len(listdomain)==3 :
        print(listdomain[1])
    elif len(listdomain)==2 :
        print(listdomain[0].split('//')[1])

DomainName('http://github.com/carbonﬁve/raygun')
DomainName('http://www.zombie-bites.com')
DomainName('https://www.cnet.com')

#number 6
def wave(kata) :
    newlist=[]
    for i in range(len(kata)) :
        kata1=''
        for j in range(len(kata)) :
            if i == j :
                kata1+=kata[j].upper()
            else :
                kata1+=kata[j].lower()
        newlist.append(kata1)
    return newlist

print(wave('jakartA'))

#number 7
def removeduplikat(kalimat) :
    kalimat = kalimat.split(' ')   
    katakata = ''
    for item in kalimat :
        if not(item in katakata) :
            katakata += (item +' ')
    print(katakata)

removeduplikat('alpha beta beta beta gamma gamma')

#number 8
def stringy(angka) :
    number=''
    for i in range(angka) :
        if((i+1)%2==0) :
            number += '0'
        elif (i+1)%2==1 :
            number +='1'
    print(int(number))

stringy(12)
stringy(3)
stringy(4)