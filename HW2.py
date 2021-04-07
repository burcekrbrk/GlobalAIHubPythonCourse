dict = {"KullanıcıAdı": "Burçe", "Şifre":1234}
a= str(input("Kullanıcı adı giriniz: "))
b= int(input("Şifre giriniz: "))

if dict["KullanıcıAdı"]==a and dict["Şifre"]==b:
    print("Tebrikler")
else:
    print("Şifre veya kullanıcı adı hatalı")