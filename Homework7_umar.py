dictionary = {}

def lihatdictionary1 (dictionary1) :
    print('================================================\n\t{:20}|\t {:1}\t\n================================================'.format('key','value'))
    i=1
    for key,value in dictionary1.items() :
        print ("{:1}.\t{:20}|\t{:1}\n".format(i,key,value))
        i+=1

def lihatdictionary() :
    lihatdictionary1(dictionary)

def isidictionary():
    jumlah = input('\nberapa kali masukan dictionary ? ')
    for j in range(int(jumlah)) :
        key = input('masukan key yang ingin ditambah ?   ')
        key = "'{}'".format(key)
        tipe = input('\njenis value apa yang ingin dimasukan ? \n1.string\n2.number\n(1/2) ')
        if tipe == '1' :
            value = (input('masukan value yang ingin ditambah ?   '))
            value ="'{}'".format(value)
            dictionary.update({key:value})
        elif tipe =='2' :
            value = int((input('masukan value yang ingin ditambah ?   ')))
            dictionary.update({key:value})
    lihatdictionary()

def caridictionary() :
    lihatdictionary()
    cari = input('\napa yang mau dicari ? ')
    tempdict={}
    for key,value in dictionary.items() :
        if cari.lower() in key.lower() :
            tempdict.update({key:value})
    lihatdictionary1(tempdict)

def keluardictionary() :
    exit()

keluar = 'y'
while keluar=='y' :
    check = False
    while (check == False ) :
        pilihmenu = input('Main Menu\n1. liat full dictionary\n2. isi dictionary\n3. searching dictionary\n4. keluar\npilih :  ')
        if ((pilihmenu =='1') or (pilihmenu=='2') or (pilihmenu == '3') or (pilihmenu == '4')) :
            check = True
        else :
            print ('pilihan salah')
    index=int(pilihmenu)-1
    menu=[lihatdictionary,isidictionary,caridictionary,keluardictionary]
    menu[index]()
    keluar=input('\nkembali ke menu utama? \n (y/n) : ')