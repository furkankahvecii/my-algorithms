# Sadece Aritmetik,Geometrik ve Karesel sayı dizisi için çalışmaktadır. 
# ? başta, ortada ve sonda yani her olasılıkta çalışır.

import math  

# Birden fazla soru işareti veya hiç soru işareti yoksa hata döndürür.
def gelenKontrol(array):
    try:
        if(len(array) <4):
            return False
        count = 0
        for each in array:
            if(each.strip() == "?"):
                count = count +1
        if(count != 1):
            return False
    except Exception as e: # handle exception
        print("Hata,", e)
    
    return True

# Arraydeki her bir elemanın başındaki ve sonundaki boşlukları temizleyen fonksiyon.
def array_strip(array):
    for index in range(len(array)-1):
        array[index] = array[index].strip()
    return array
    
# Aritmetik sayı dizisi olup olmadığını kontrol eden fonksiyon
def is_arithmetic(l, diff, indexSoruIsareti):
    find = 0
    for index in range(len(l) - 1):
        if(index == indexSoruIsareti):
            find = l[index] - diff;
        elif(index + 1 == indexSoruIsareti):
            if not ((l[index+1] - l[index]) /2 == diff):
                return False
            else: 
                find = l[index+1] - diff;
        else:
            if not (l[index + 1] - l[index] == diff):
             return False

    return (l[len(l)-1] + diff) if indexSoruIsareti == len(l)  else find;

# Geometrik sayı dizisi olup olmadığını kontrol eden fonksiyon
def is_geometric(l, diff, indexSoruIsareti):
    find = 0
    for index in range(len(l) - 1):
        if(index+1 == indexSoruIsareti):
            if not ((l[index+1] / l[index]) == diff * diff):
                return False
            else: 
                find = l[index+1] / diff;
        elif(index == indexSoruIsareti):
            find = l[index] / diff;
        else:
            if not (l[index + 1] / l[index] == diff):
                return False
    if(indexSoruIsareti == len(l)):
        if(l[len(l)-2] > l[len(l)-1]):
            return l[len(l)-1] * diff;
        else:
            return l[len(l)-1] / diff if diff < 1 else l[len(l)-1] * diff;
            
    return find  

# Karesel sayı dizisi olup olmadığını kontrol eden fonksiyon
def is_karesel(l, diff, indexSoruIsareti):
    find = 0
    for index in range(len(l) - 1):
        if(index+1 == indexSoruIsareti):
            if not ((math.sqrt(l[index+1]) - math.sqrt(l[index])) == diff + diff):
                return False
            else: 
                find = (math.sqrt(l[index+1]) -diff) ** 2;
        elif(index == indexSoruIsareti):
            find = (math.sqrt(l[index])-diff) ** 2;
        else:
            if not (math.sqrt(l[index + 1]) - math.sqrt(l[index]) == diff):
             return False
    if(indexSoruIsareti == len(l)):
        return (math.sqrt(l[len(l)-1]) + diff ) ** 2;
        
    return find  

# Girilen dizinin türünü bulmaya yarayan fonksiyon.
def turBul(array, indexSoruIsareti):
    
    try:
        # Her bir dizi türünün elemanları arasında ki farkı hesaplamak farklıdır.
        if(indexSoruIsareti != 0 and indexSoruIsareti != 1):
            aritmetik_fark = array[1] - array[0]
            geometrik_fark = array[1] / array[0]
            karesel_fark = math.sqrt(array[1]) - math.sqrt(array[0])
        else:
            aritmetik_fark = array[len(array)-1] - array[len(array)-2]
            geometrik_fark = array[len(array)-1] / array[len(array)-2]
            karesel_fark = math.sqrt(array[len(array)-1]) - math.sqrt(array[len(array)-2])
    except Exception as e: # handle exception
        print("Hata = ", e)
        return

    isArit = is_arithmetic(array, aritmetik_fark, indexSoruIsareti)
    if(type(isArit) != type(True)): # isArit boolean bir degermi?
        print("Dizi aritmetik sayı dizisidir")
        print("Bilinmeyen sayının değeri = ", isArit)
        return
    
    isGeo = is_geometric(array, geometrik_fark, indexSoruIsareti)
    if(type(isGeo) != type(True)):
        print("Dizi geometrik sayı dizisidir")
        print("Bilinmeyen sayının değeri = ", int(isGeo))
        return
  
    isKaresel = is_karesel(array, karesel_fark, indexSoruIsareti)
    if(type(isKaresel) != type(True)):
        print("Dizi karesel sayı dizisidir")
        print("Bilinmeyen sayının değeri = ", int(isKaresel))
        return
    
    print("Girilen sayı dizisi herhangi bir türe ait bulunamadi.")


#Arithmetic
#array = "1,5,9,13,17,?".split(",")
#array = "?,10,20,30,40".split(",")
#array = "80,50,20,-10,?".split(",")

#Geometric
#array = "?,6,18,54,162,486".split(",")
#array = "320, 160, 80, 40, 20, ?".split(",")
#array = "100,1000,10000,?".split(",")

#Ucgensel
#array = "1,3,6,10,15,21,28,36".split(",")

#Karesel
#array = "1,4,9,?,25,36".split(",")
#array = "?,49,100,169,256".split(",")
#array = "16,49,100,169,256,?".split(",")

array = input("Sayı Dizisini Giriniz: ").split(",")

if(gelenKontrol(array)):
    array = array_strip(array);
    print(array)
    indexSoruIsareti = array.index("?")
    del array[indexSoruIsareti]
    array = list(map(int, array)) 
    turBul(array, indexSoruIsareti)
else:
    print("Girilen değerde bir hata var.")