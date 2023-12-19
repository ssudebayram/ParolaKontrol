sayi = 1
while sayi <= 5:
    cevap = int(input("Parolanızı giriniz: "))
    if cevap == 123:
        print("Girdiğiniz parola doğru")
        break
    else:
        print("Girdiğiniz parola yanlış")
    sayi += 1
else:
    print("\nGiriş hakkınız bitmiştir.")
