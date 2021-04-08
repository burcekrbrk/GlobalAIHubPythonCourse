#1. ödevin a şıkkı
liste = [1, 2, 3, 4, 5, 6]
a = len(liste)

liste1= liste[int(a/2):]
liste2= liste[:int(a/2)]
print(liste1 + liste2)

#1. ödevin b şıkkı
n = int(input("Tek basamaklı bir sayı giriniz"))
for i in range(0,n+1,2):
    print(i)