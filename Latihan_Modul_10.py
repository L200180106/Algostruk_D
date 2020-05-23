###10.1 Menjumlahkan bilangan 1 sampai n
import time
## Jumlah Cara Pertama
def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range (1, n+1):
        hasilnya += i
    return hasilnya

for i in range(5):                  #mengulang lima kali
    awal = time.time()              #menandai awal kerja
    h = jumlahkan_cara_1(1000000)   #menjumlah 1 sampai sejuta
    akhir = time.time()             #menandai akhir kerja, lalu mencetak
    print("Jumlah adalah %d,memerlukan %9.8f detik" % (h, akhir-awal))

## Jumlah Cara Kedua
import time
def jumlahkan_cara_2(n):
    return (n*(n+1))/2

for i in range(5):                 #mengulang lima kali
    awal = time.time()             #menandai awal kerja
    h = jumlahkan_cara_2(1000000)  #menjumlah 1 sampai sejuta
    akhir = time.time()            #menandai akhir kerja, lalu mencetak
    print("Jumlah adalah %d,memerlukan waktu %9.8f detik" % (h, akhir-awal))

###10.3 Kasus terburuk, rata-rata, dan terbaik
import time
import random

def insertionSort(a):
    for i in range(1, len(a)):
        nilai = a[i]
        b = i
        while b >0 and nilai<a[b - 1]:
            a[b] = a[b-1]
            b -=1
        a[b] = nilai

print("--------------Average Case Scenario---------------")    
## Average Case
for i in range(5):
    L = list(range(3000))
    random.shuffle(L)
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Mengurutkan %d bilangan, memerlukan waktu %8.7f detik" % (len(L),akhir-awal))
## Worst Case
print("---------------Worst Case Scenario-----------------") 
for i in range(5):
    L = list(range(3000))
    L = L[::-1]
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Mengurutkan %d bilangan, memerlukan waktu %8.7f detik" % (len(L),akhir-awal))
## Best Case
print("---------------Best Case Scenario------------------") 
for i in range(5):
    L = list(range(3000))
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Mengurutkan %d bilangan, memerlukan waktu %8.7f detik" % (len(L),akhir-awal))

###10.4 Menganalisis kode python
## Operasi Dasar
x = 5
y = x
z = x + y * 8
d = x > 0 and x < 100
f = [3,2,4,5]
v = f[0:2]
print("x = ", x)
print("y = ", y)
print("z = ", z)
print("d = ", d)
print("f = ", f)
print("v = ", v)

## Kode yang mempunyai kompleksitas
count = 0
i = 32
while i >= 1 :
    count += 1
    i = i // 2
    print("i = ", i, " ", "count = ", count)

print(count)

###10.5 Analisis pewaktuan menggunakan timeit
from timeit import timeit
print(timeit('sqrt(2)', 'from math import sqrt', number=10000))

print(timeit('sqrt(2)', 'from math import sqrt', number=100000))

print(timeit('sqrt(2)','from math import sqrt',number = 10000))

print(timeit("1+2"))#waktu untuk menghitung 1+2, diulang 1 juta kali

print(timeit("sin (pi/3)", setup = "from math import sin,pi"))
##sin(pi/3), diulang 1 juta kali

print(timeit("sin (1.047)", setup = "from math import sin"))
##sin(1.047), diulang 1 juta kali


###10.5.1 Melihat O(n2) pada nested loop
import timeit
import matplotlib.pyplot as plt

## Ini fungsi nested loop yang akan diuji:
def kalangBersusuh(n):
    for i in range(n):
        for j in range (n):
            i+j

## Ini fungsi pengujinya:
def ujiKalangBersusuh(n):
    ls = []
    jangkauan = range(1,n+1)
    siap = "from __main__ import kalangBersusuh"
    for i in jangkauan:
        #print('i = ',i)
        t=timeit.timeit("kalangBersusuh(" +str(i) +")",setup=siap,number=1)
        ls.append(t)
    return ls

## Pemanggilan pengujian
n = 1000
LS = ujiKalangBersusuh(n) #dari 1 sampai 1000
#LS adalah list hasil uji kecepatan, dari n sedikit ke banyak
## Menggambar grafik. Di bawah ini saja yang diulang saat me-nyetel skala
plt.plot(LS)     #mem-plot hasil uji
skala = 7700000  #<----- setel skala ini sesuai hasilmu
plt.plot([x*x/skala for x in range (1,n+1)]) #grafik x^2 untuk pembanding
plt.show()       #tunjukkan plotnya
