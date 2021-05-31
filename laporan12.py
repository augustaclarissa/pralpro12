#Augusta Clarissa Silvy Pascalin
#Universitas Kristen Duta Wacana
#Topik : Fungsi Rekursif

'''Pak Julius Karel memiliki keinginan untuk membuat kalkulator FPB agar saat mengajar mata kuliah
Matematika Diskrit menjadi lebih mudah dan tidak memakan waktu yang banyak.'''

#input : bil1, bil2
#proses : jika bil2 = 0 maka hasilnya bil1, jika bukan maka menggunakan hasil sisa bagi
#output : Hasil FPB

bil1 = int(input("Masukkan bilangan pertama : "))
bil2 = int(input("Masukkan bilangan kedua : "))

def fpb(bil1,bil2):
    if bil2 == 0:
        return bil1
    else:
        return fpb(bil2, bil1%bil2)

print("Maka hasil FPB dari ", bil1, "dan", bil2, "adalah", fpb(bil1,bil2))