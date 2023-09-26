#Studi Kasus Saldo dan Utang
print()
saldo_awal = input('Saldo Awal Anda : ')
print('Saldo anda : ' + str(saldo_awal))
deposit = input('Saldo yang di deposit : ' )

print()
tot = (int(saldo_awal) + int(deposit))
print('Saldo Anda : ' + str(tot))
print()

hutang  = input('Utang saat ini: ')
hutang = (tot - int(hutang))
print('Saldo sisa Anda : ' + str(hutang))
print()

if hutang <= 50000 :
    print('Saldo anda saat ini sisa : ' + str(hutang))
    print('Selamat anda terjerumus miskin')
    print()

else :
    print('Saldo anda saat ini : ' + str(hutang))
    print('Selamat ada sedang dalam kemiskinan')
    print()

