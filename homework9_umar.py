data1=["jhon","smith","01-jan-1967","m"]
data2=["steve","jobs","23-jan-2010","m"]

def generatenum (data) :
    num = ''
    a=len(data[1])
    num += data[3].upper()
    num += data[0][0].upper()
    num += data[1][0].upper()
    if a%2==1 :
        num+=data[1][(a//2)].upper()
    elif a%2==0 :
        num += (data[1][(a//2)-1].upper()+data[1][(a//2)].upper())
    date1=data[2].split('-')
    num += '-{}'.format(date1[0][1])
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    num += str(months.index(date1[1]) + 1)
    num += date1[2][2] + date1[2][3]
    print(num)

generatenum(data2)
generatenum(data1)

def finduniq(listangka) :
    hasil=[]
    uniq = 'maka angka yang uniq adalah '
    angka= {item : 0 for item in listangka}
    for key in angka :
        much = 0
        for item in listangka :
            if key == item :
                much +=1
        angka[key] = much
    for key in angka :
        if angka[key]==1 :
            hasil.append(str(key))        
    if len(hasil) == 0 :
        print('nothing')
    else :
        for i in range(len(hasil)) :
            if i == (len(hasil)-2) :
                uniq += '{} dan '.format(str(hasil[i]))
            else :
                uniq += '{} '.format(str(hasil[i]))
        print(uniq)

finduniq([1,3,1,2,1,1])
finduniq([1,2,1,2,1,1])
finduniq([0,0,0.55,0,0])


def sumtwosmallets(listangka) :
    if listangka[0] < listangka[1] :
        smallets1 = listangka[0]
        smallets2 = listangka[1]
    else :
        smallets1 = listangka[1]
        smallets2 = listangka[0]
    for i in range(2,len(listangka)) :
        if smallets1>listangka[i] :
            smallets2 = smallets1
            smallets1 = listangka[i]
        elif smallets2>listangka[i] :
            smallets2 = listangka[i]
    print ('dua angka terkecil adalah {} dan {}, jumlahnya adalah {}'.format(smallets1,smallets2,(smallets1+smallets2)))
sumtwosmallets([19,5,42,2,77])


def numberofpairs(mylist) :
    a=mylist
    mybox = {item : 0 for item in a}
    pairs = 0
    for key in mybox :
        much = 0
        for item in a :
            if key==item :
                much +=1
        mybox[key] = much
        pairs += (much//2)
    print(pairs)  
    print(mybox)

numberofpairs(['red','green','red','blue','blue','blue','blue'])
