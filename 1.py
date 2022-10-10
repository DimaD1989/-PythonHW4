# Вычислить число c заданной точностью d

# Пример:
# n = float(input("Введите  число: "))
# print(round(n,3))

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# n = int(input("Введите натуральное число: "))
# Fact = []
# d = 2
# m = n # Запомним исходное число
# while d * d <= n:
#         if n % d == 0:
#             Fact.append(d)
#             n//=d
#         else:
#             d += 1
# Fact.append(n) # Добавим последнеё простое число
# print('{} = {}' .format(m, Fact)) # Выводим исходное число и все простые множители.
# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# numbers = [10, 20, 20, 30, 30, 4, 5]
# list_of_unique_numbers = []
# for i in numbers:
#     b=0
#     for j in numbers:
#         if i==j:
#             b+=1
#     if b==1:
#         list_of_unique_numbers.append(i)
# print('{} = {}' .format(b,list_of_unique_numbers))

# numbers = [10, 20, 20, 30, 30, 4, 5]
# list_of_unique_numbers = []
# for i in numbers:
#  if numbers.count(i)==1:
#     list_of_unique_numbers.append(i)
# print(list_of_unique_numbers)
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# from random import random
# from unittest import result


# k=2
# a=round(random()*10)
# b=round(random()*10)
# c=round(random()*10)
# print(a,b,c)
# result=""
# if b==0: result= f"{a}*x**{k} + {c}*x**{k-1}=0"
# if b==0 and c ==0: result= f"{a}*x**{k}=0"
# if c==0: result= f"{a}*x**{k}+{b}*x**{k-1}=0"
# else: result = f"{a}*x**{k}+{b}*x**{k-1}+{c}*x**{k-2}=0"
# with open("file.txt", "w") as file1:
#     file1.write(result)
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.
# 