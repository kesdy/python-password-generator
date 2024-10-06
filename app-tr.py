import random
import string

def parola_olusturucu(uzunluk=12, buyuk_harf_kullan=True, rakam_kullan=True, sembol_kullan=True):
    # Temel karakter setini oluştur
    karakterler = string.ascii_lowercase  # Küçük harfler
    
    if buyuk_harf_kullan:
        karakterler += string.ascii_uppercase  # Büyük harfler
    if rakam_kullan:
        karakterler += string.digits  # Rakamlar
    if sembol_kullan:
        karakterler += string.punctuation  # Semboller

    # Rastgele bir parola oluştur
    parola = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return parola

# Parola uzunluğunu ve karakter türlerini belirt
uzunluk = int(input("Parola uzunluğunu girin: "))
buyuk_harf_kullan = input("Büyük harfler dahil edilsin mi? (e/h): ").lower() == 'e'
rakam_kullan = input("Rakamlar dahil edilsin mi? (e/h): ").lower() == 'e'
sembol_kullan = input("Semboller dahil edilsin mi? (e/h): ").lower() == 'e'

# Parolayı oluştur
olusturulan_parola = parola_olusturucu(uzunluk, buyuk_harf_kullan, rakam_kullan, sembol_kullan)
print("Oluşturulan Parola:", olusturulan_parola)
