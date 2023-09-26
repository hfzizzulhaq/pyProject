#           VARIABLE AND DATE 
#Strings
#age = 21
#student = 12
#people = 30 
#print(f"Your Age {age} Years Old")
#print(f"Total {student} student")
#print(f"Muslim People is {people}")

#float 
#gpa = 3.5
#hight =  1.8 
#price = 10.50
#print(f"My GPA is {3.5}")
#print(f"Your hight is {hight} meters")
#print(f"For Rice {price} USD")

#boolean
#online = True
#for_sale = False
#running = False
#print(f'are you onlline?: {online}')
#print(f'is the item for sale?; {for_sale}')
#print(f'Game running: {running}')

#if running :
    #print('The game is running')
#else :
    #print('The game is over')



#    TYPECASTING PYTHON
#name = input('Yor name: ')
#age = input('Your Age: ')
#gpa = float(input('Your Gpa: '))

#print()
#print(f"Hello Bro/Sis {name}")
#print(f"You Are {age} years old ")
#print()
#if gpa > 3 :
 #   print(" Congratulation For You")
#else :
 #   print("anda tidak lulus dan anda harus Mengulang bangsat")

#length = float(input('enter the length : '))
#widht = float(input('enter the width : '))
#height = float(input('enter the height : '))

#volume = length * widht * height

#print(f'the area of reactangle is {volume} cm^2')



#item = input('What item would you buy? : ')
#price = float(input('How much the price for the item? : '))
#quantity = int(input('How many would you buy for the item? : '))
#money = float(input('Your Money is : '))

#otal1= price * quantity
#total2= money - total1

#print(f'You buy {item} in mini market')
#print(f'Price for 1 item is {price} USD')
#print(f'You buy {quantity} items')
#print(f'Total price you buy is {round(total1, 2)} USD')
#rint(f'you hava chnages is {round(total2, 2)} USD')
#print(f'Happy shopping for you')


#   SIMPLE CALCULATOR PROGRAM
#operator = input('Enter The Operator (+ - * /) : ')
#num1 = float(input('Enter the 1st Number : '))
#num2 = float(input('Enter the 2st Number : '))

#if operator == "+" :
#    result1 = num1 + num2
#    print(result1)
#elif operator == '-' :
#    result2 = num1 - num2
#    print(result2)
#elif operator == '*' :
#    result3 = num1 * num2
#    print(result3)
#elif operator == "/" :
#   result4 = num1 / num2
#    print(result4)
#else :
#    print(f'{operator}  in not valid operator')



#Simpel Convertion Calculation
#Temp = float(input('Masukkan Nilai Temperatur (C / F / K / R) : '))
#Unit_Conv = input('Masukkan Unit Yang Ingin di Konversi : ')

#f Unit_Conv == 'F to C' :
#    Temp = 5/9 * (Temp - 32)
#    Unit_Conv = 'Celcius'
#    print(f'Untuk Hasil {round(Temp, 2)} C')
#elif Unit_Conv == 'F to R' :
#    Temp = 4/9 * (Temp - 32)
#    Unit_Conv = 'Reamur'
#    print(f'Untuk Hasil {round(Temp, 2)} R')
#elif Unit_Conv == 'C to F' :
#    Temp = 9/5 * (Temp - 32)
#    Unit_Conv = 'Fahrenheit'
#    print(f'Untuk Hasil {round(Temp, 2)} F')
#elif Unit_Conv == 'C to K' :
#    Temp = Temp + 273
#    Unit_Conv = 'Kelvin'
#    print(f'Untuk Hasil {round(Temp, 2)} K')
#elif Unit_Conv == 'C to R' :
#    Temp = 4/5 * Temp
#    Unit_Conv = 'Reamur'
#    print(f'Untuk Hasil {round(Temp, 2)} R')
#elif Unit_Conv == 'R to C' :
#    Temp = 5/4 * Temp
#    Unit_Conv = 'Celcius'
#    print(f'Untuk Hasil {round(Temp, 2)} C')
#elif Unit_Conv == 'R to F' :
#    Temp = 9/4 * (Temp + 32)
#    Unit_Conv = 'Fahrenheit'
#    print(f'Untuk Hasil {round(Temp, 2)} F')
#elif Unit_Conv == 'R to K' :
#    Temp = 5/4 * (Temp + 273)
#    Unit_Conv = 'Kelvin'
#    print(f'Untuk Hasil {round(Temp, 2)} K')
#elif Unit_Conv == 'K to C' :
#    Temp = Temp - 273
#    Unit_Conv = 'Celcius'
#    print(f'Untuk Hasil {round(Temp, 2)} C') 
#elif Unit_Conv == 'K to R' :
#    Temp = 4/5 * (Temp - 273)
#    Unit_Conv = 'Reamur'
#    print(f'Untuk Hasil {round(Temp, 2)} R')
#else :
#    print(f'{Unit_Conv} tidak tervalidasi' )


# Validate exerciese 
# 1.Username is no more than 12 characters
# 2.Username must not contain space
# 3.Username must not contain digit 
#username = input('Enter a username : ')

#if len(username) < 12 :
#    print('Your name must be 12 characters')
#elif not username.find('  ') == -0 :
#    print('username cant contain the spaces')
#elif not username.isalpha() :
#    print('username cant contain a number')
#else :
#    print(f'Welcome {username}')


#principle comound interest calculator
#for loop
#principle = 0
#rate = 0
#time = 0

#while principle <= 0:
#    principle = float(input("Enter the interest principle : "))
#    if principle <= 0:
#        print("The principle can't be less than or equal zero")

#while rate <= 0:
#    rate = float(input("Enter the interest rate : "))
#    if rate <= 0:
#       print("The rate can't be less than or equal zero")

#while time <= 0:
#    time = int(input("Enter the time in years: "))
#    if time <= 0:
#        print("The time can't be less than or equal zero")

#final_amount = principle * pow((1+ rate / 100), time)
#print(f'Balance after {time} year/s ${round(final_amount, 2)}')


#Nested Loop = A loop within another loop (outer, inner) outer loop
#row = int(input("enter the row : "))
#columns = int(input("enter the columns : "))
#symbol = input("enter a symbol : ") 

#for x in range(row) :
#    for y in range(columns) :
#        print(symbol, end="")
#    print()

import time
