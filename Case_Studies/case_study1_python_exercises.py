############################################################
# Pyhton
############################################################
# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız.
text = "The goal is to turn data into information, and information into insight"

letter_list = []
text = text.replace(',', '').upper()

for std in text.split():
    letter_list.append(std)
print(letter_list)

# alternatif çözüm
# letters = [letter for letter in text.split()]

# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]
def division(numbers_list):
    even_list = []
    odd_list = []
    for n in numbers_list:
        if n % 2 == 0:
            even_list.append(n)
        else:
            odd_list.append(n)
    return even_list, odd_list

even_list, odd_list = division(l)
print("even list: ", even_list)
print("odd list: ", odd_list)


#Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
# bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
for index, std in enumerate(students):
    if students[index] in students[:3]:
        print('Mühendislik Fakültesi: ', index+1, ". öğrenci: ", std)
    else:
        print('Tıp Fakültesi: ', index-2, ". öğrenci: ", std)
    # elif students[index] in students[-3:]:
    #     print('Tıp Fakültesi: ', index, ". öğrenci: ", std)


# Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
# almaktadır. Zip kullanarak ders bilgilerini bastırınız.
ders_kodu = ["ABC123", "DEF456", "GHI789", "JKL012"]
kredi = [3, 4, 5, 6]
kontenjan = [30, 75, 150, 25]
ders_bilgileri = list(zip(ders_kodu, kredi, kontenjan))
for lst in ders_bilgileri:
    print("Kredisi", lst[1], "olan", lst[0], "kodlu dersin kontenjanı", lst[2], "kişidir.")

# alternatif çözüm
# for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
#     print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")


# Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "pyhton"])
kume2 = set(["data","function","qcut","lambda", "pyhton", "miuul"])

def kumeler(kume1, kume2):
    if kume1.issuperset(kume2):
        print("kume1 kume2' yi kapsar")
        print(f"ortak elemanlar: {kume1.intersection(kume2)}")
    else:
        print("kume1 kume2' yi kapsamaz")
        print(f"kume2' nin kume1'den farkı: {kume2.difference(kume1)}")

kumeler(kume1,kume2)
kumeler(kume2,kume1)

