visocos = int(input("Пожалуйста, введите годик циферками: "))

def Dni_v_godushke(maslo):  

    resultatic = 0
    i = 0

    while i<12:
        while maslo[i]>0:

            resultatic += maslo[i] // 10 + maslo[i] % 10 
            maslo[i] -= 1

        i += 1

    return resultatic


maslo = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (visocos%100 != 0):
    
    if (visocos%4 == 0):
        maslo = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
elif (visocos%400 == 0):
    maslo = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
print(Dni_v_godushke(maslo))

    #num = int(input("Введите целое: "))
#sum = 0
#while (num != 0):
  #  sum = sum + num % 10
   # num = num // 10
#print("Сумма цифр числа равна: ", sum)