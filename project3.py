baris = int(input('Jumlah baris : '))
kolom = int(input('Jumlah kolom : '))
merek = (input('Merek: '))

for x in range (kolom):
    for y in range (baris):
        print(merek, end=' ')
    print()