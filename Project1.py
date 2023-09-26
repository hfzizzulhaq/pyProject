#Studi Kasus Nilai Ujian Sekolah
#Penggunaan Python Condition

nilai_ujian_IPA = 70
nilai_ujian_IPS = 67
nilai_ujian_BTQ = 96

tot = int( (nilai_ujian_IPA + nilai_ujian_IPS + nilai_ujian_BTQ) / 3 )
print()
print('Nilai Anda adalah : '+ str(tot))

if tot <= 75 :
    print('Tidak Lulus')
    print()

elif tot <= 80 :
    print('hampir sempurna')
    print()

elif tot <= 90 :
    print('Nilai Sempurna')
    print()

else :
    print('Anda terlalu OP')
    print()
