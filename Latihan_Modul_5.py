def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
K = [50,20,70,10]
##swap(K,1,3)
##print(K)

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini            #-> anggap ini yang terkecil
    for i in range(dariSini+1, sampaiSini):  #-> cari di sisa list
        if A[i] < A[posisiYangTerkecil]:     #-> kalau menemukan yang lebih kecil
            posisiYangTerkecil = i           #-> anggap diubah
    return posisiYangTerkecil
A = [18,13,44,25,66,107,78,89]
##j = cariposisiterkecil(A,2,len(A))
##print(j)

def kecil(a):
    ter = 0
    for i in range(ter,len(a)):
        if a[i] < a[ter]:
            ter = i
    return ter
##f = kecil(A)
##print(f)

#5.1 Bubble Sort 
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):       #->Lakukan operasi gelembung sebanyak n-1
        for j in range(n-i-1): #->Dorong elemen terbesar ke ujung kanan
            if A[j] > A[j+1]:  #->Jika di kiri lebih besar dari di kanannya,
                swap(A,j,j+1)  #>tukar posisi elemen ke j dengan ke j+1
##bubblesort(A)
##print(A)

#5.2 Selection Sort 
def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)
##selectionsort(K)
##print(K)
            
#5.3 Insertion Sort
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]: #->Cari posisi yang tepat
            A[pos] = A[pos-1]               #   dan geser ke kanan terus
            pos = pos-1                     #   nilai - nilai yang lebih besar
        A[pos] = nilai                      #->Pada posisi ini ditempatkan nilai elemen ke i.
P=[10,51,2,18,4,31,13,5,23,64,29]
##insertionsort(P)
##print(P)
