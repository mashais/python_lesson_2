# lesson_2_homework
# Задачи на циклы и операторы условия


#Задача 1
# Вывести на экран циклом 5 строк из нулей, причем каждая строка должна быть пронумерована

for i in range(1, 5 + 1):
         print(i,'000000000')




# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.

print('Input Digits')
d = 5
count = 0
for i in range(1, 10 + 1):
    m = int(input('Digit ' + str(i) + ':'))
    while m > 0:
        if m%10 == d:
            count += 1
        m = m // 10
print((count), ('Digits 5'))





# Задача 3
#Найти сумму чисел от 1 до 100. Полученный результат вывести на экран.

sum = 0

for i in range(1,101):
      sum+=i
print(sum)




# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.


mult = 1

for i in range(1,11):
      mult*=i
print(mult)



# Задача 5
# Вывести цифры числа на каждой строчке.

integer_number = 2129
while integer_number>0:
      print(integer_number%10)
      integer_number = integer_number//10



# Задача 6
# Найти сумму цифр числа.


print('Input Number:')
n = input()
sum = 0
for i in n:
      sum += int(i)
print(sum)



# Задача 7
# Найти произведение цифр числа.


print('Input Number:')
n = input()
mult = 1
for i in n:
     mult = mult * int(i)
print(mult)



# Задача 8
#Дать ответ на вопрос: есть ли среди цифр числа 5?


integer_number = 297363
while integer_number>0:
      if integer_number%10 == 5:
            print('Yes')
            break
      integer_number = integer_number//10
else:print('No')



# Задача 9
# Найти максимальную цифру в числе

a = int(input('Input number:'))
m = a%10
a = a // 10
while a> 0:
    if a%10 > m:
        m = a%10
    a = a//10
print (m)



# Задача 10
# Найти количество цифр 5 в числе

integer_number = 55599
d = 5
count = 0
while integer_number > 0:
    if integer_number%10 == d:
        count += 1
    integer_number = integer_number // 10
print(count, 'Digit 5')