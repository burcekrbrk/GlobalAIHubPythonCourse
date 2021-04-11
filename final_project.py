dict= {"a":["Hatay'ın plakası kaçtır?", 31],
        "b":["Türkiye kaç coğrafi bölgeden oluşur?", 7],
        "c":["Araba sevdasının yazarı kimdir?","Recaizade Mahmud Ekrem"],
        "d":["Yerli otomobilimizin ismi nedir?","TOGG"],
        "e":["Aya ilk hangi yıl ayak basılmıştır?", 1969],
        "ç":["Künefesiyle hangi ilimiz meşhurdur?","Hatay"],
        "f":["Alfabemiz kaç harften oluşur?", 29],
        "h":["Antep'in ünlü tatlısı","baklava"],
        "k":["Yedigöller hangi ilimizdedir?","Bolu"],
        "m":["Güneş sistemimizdeki en büyük gezegen","Jüpiter"]}
       
def burc():
    sayı=0
    print("1.soru:", dict["a"][0])

    a1 = int(input("1. cevabınız: "))
    if a1==dict["a"][1]:
        print("True")
        sayı=sayı+10
    else:
        print("False")

    print("2.soru:", dict["b"][0])
    a2 = int(input("2. cevabınız: "))
    if a2==dict["b"][1]:
        print("True")
        sayı=sayı+10
    else:
        print("False")

    print("3.soru:", dict["c"][0])
    a3 = input("3. cevabınız: ")
    if a3==dict["c"][1]:
        print("True")
        sayı=sayı+10
    else:
        print("False")

    print("4.soru:", dict["d"][0])
    a4 = input("4. cevabınız: ")
    if a4==dict["d"][1]:
        print("True")
        sayı=sayı+10
    else:
        print("False")

    print("5.soru:", dict["e"][0])
    a5 = int(input("5. cevabınız: "))
    if a5==dict["e"][1]:
        print("True")
        sayı=sayı+10
    else:
        print("False")

    print("6.soru:", dict["ç"][0])
    a6 = input("6. cevabınız: ")
    if a6==dict["ç"][1]:
        print("True")
        sayı=sayı+10
    else:
        print("False")

    print("7.soru:", dict["f"][0])
    a7 = int(input("7. cevabınız: "))
    if a7==dict["f"][1]:
        print("True")
        sayı=sayı+10
    else:
        print("False")

    print("8.soru:", dict["h"][0])
    a8 = input("8. cevabınız: ")
    if a8==dict["h"][1]:
        print("True")
        sayı=sayı+10
    else:
        print("False")

    print("9.soru:", dict["k"][0])
    a9 = input("9. cevabınız: ")
    if a9==dict["k"][1]:
        print("True")
        sayı=sayı+10
    else:
        print("False")

    print("10.soru:", dict["m"][0])
    a10 = input("10. cevabınız: ")
    if a10==dict["m"][1]:
        print("True")
        sayı=sayı+10
    else:
        print("False")

    if sayı >=50:
        print("Successful, your result: ",sayı)
    else:
        print("Unsuccessful, your result: ",sayı)
burc()

