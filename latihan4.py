#Raka Emillul Fata
#Latihan 4 : Perbandingan Linear Search dan Nested Loop

#Linear Search (O(n))
data   = [1,3,5,7,9,11,13]
target = int(input("Cari angka: "))
count  = 0

for item in data:
    count += 1
    if item == target:
        break

print("Jumlah langkah: ", count)

#Nested Loop
data  = [1,3,5,7,9]
count = 0

for i in data:
    for j in data:
        count += 1

print("Jumlah langkah: ", count)