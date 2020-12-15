from random import randint

kolon = int(input("Kolon sayiniz: "))
if(kolon >= 0):
       
    liste = []
    count = 0;
    sayi_adet = 6
    rand_min = 1
    rand_max = 10
    
    if((rand_max - rand_min) < sayi_adet ):
        print("Random araligin, bir kolonda bulunmasi gereken adetten fazla olmalidir.")
        exit()
    
    while(count < kolon):
        i = 0
        alt_liste = []
        while(i < sayi_adet):
            random_sayi = randint(rand_min, rand_max)
            while(random_sayi in alt_liste):
                random_sayi = randint(rand_min, rand_max)
            
            alt_liste.append(random_sayi)
            i = i + 1
        liste.append(alt_liste)
        count = count +1
    
    print(liste)

else:
     print("Kolon sayisi negatif olamaz.")