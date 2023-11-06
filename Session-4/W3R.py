# 2
# import sys
# print(sys.version)
# print(sys.version_info)


# 3
# import datetime
# date = datetime.datetime.now()
# print(date.strftime("%Y-%m-%d %H:%M:%S"))


# 4
# r = float(input("enter the radius > "))
# area = 3.14 * r * r
# print(area)


# 5
# firstNAme = input("enter your first name > ")
# secondName = input("enter your second name > ")
# print(secondName + " " + firstNAme)


# 6
# value = input("enter seq of number > ")
# List = value.split(",")
# T = tuple(List)
# print(List)
# print(T)


# 7
# file = input("enter the file name > ")
# arr = file.split(".")
# print(arr[-1])


# 8
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0] + "  " + color_list[-1])


# 9
# exam_st_date = (11, 12, 2014)
# print("%i / %i / %i  " % exam_st_date)


# 10
# n = float(input("enter a number > "))
# n1 = float("%i" % n)
# n2 = float("%i%i" % (n, n))
# n3 = float("%i%i%i" % (n,n,n))
# print(n1 + n2 + n3)


# 11
# print(abs.__doc__)


# 12
# import calendar
# month = int(input("enter the month > "))
# year = int(input("enter the year > "))
# print(calendar.month(year, month))


# 13
# print("""a string you don't have to escape
# This
# is a ... multi-line
# heredoc string ------> example
# """)


# 14
# from datetime import date
# d1 = date(2014, 7, 2)
# d2 = date(2016, 7, 11)
# diff = d2 - d1
# print(diff.days)


# 15
# r = float(input("enter the radius > "))
# volume = 4/3 * 3.14 * r**3
# print(volume)


# 16
# num = int(input("enter a number > "))
# diff = num - 17
# if num > 17:
#     print(2*diff)
# else:
#     print(abs(diff))


# 17
# def near(num):
#     return (abs(1000 - num) <= 100) or (abs(2000 - num) <= 100)
#
# print(near(1101))


# 18
# num1 = int(input("enter a number > "))
# num2 = int(input("enter a number > "))
# num3 = int(input("enter a number > "))
# sum = num1 + num2 + num3
#
# if num1 == num2 == num3:
#     print(sum *3)
# else:
#     print(sum)


# 19
# x = input("enter a text > ")
# y = x.split()
# if y[0] == "Is":
#     print(x)
# else:
#     print("Is " + x)


# 20
# x = input("enter a text > ")
# n = int(input("numbers of copies > "))
# res = ""
# for i in range(n):
#     res += x
#
# print(res)


# 21
# x = int(input("enter a text > "))
# if x % 2 == 0:
#     print("even number")
# else:
#     print("odd number")


# 22
# x = [1,2,3,4,4,4,4,5,5,6,8,9]
# count = 0
#
# for i in x:
#     if i == 4:
#         count += 1
#
# print(count)


# 23
# def copy(str, n):
#     res = ""
#     if len(str) < 2:
#         for i in range(n):
#             res += str
#     else:
#         sub = str[:2]
#         for i in range(n):
#             res += sub
#     return res
#
# print(copy("y",5))


# 24
# x = input("enter a character > ")
# s = ["a", "e", "i", "u", "o"]
# if x in s:
#     print("vowel")
# else:
#     print("not vowel")


# 25
# def test(data,n):
#     if n in data:
#         return True
#     else:
#         return False
#
# print(test([1, 2, 3, 4 ,5], 5))


# 26
# x = [2, 3, 6, 5]
#
# for i in x:
#     while i > 0:
#         print("@", end = " ")
#         i = i - 1
#     print("\n", end="")


# 27
# x = ["a", "b", "c", "d"]
# for i in x:
#     print(i , end="")


# 28
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
#
# for i in numbers:
#     if i == 237:
#         print(i)
#         break
#     elif i % 2 == 0:
#          print(i, end=" ")


# 29
# color_list_1 = {"White", "Black", "Red"}
# color_list_2 = {"Red", "Green"}
# print(color_list_1 - color_list_2)


# 30
# base = int(input("enter a base > "))
# height = int(input("enter a height > "))
# print(0.5 * base * height)


# 31
# import math
# print(math.gcd(360,336))


# 32
# import math
# print(math.lcm(360,336))


# 33
# def sum(x, y ,z):
#     sum = 0
#     if x == y or x == z or y == z:
#         sum = 0
#     else:
#         sum = x + y + z
#
#     return  sum
#
#
# print(sum(2,2,3))


# 34
# def sum(x, y):
#     sum = x + y;
#     if sum > 15 and sum < 20:
#         return 20
#     else:
#         return sum
#
# print(sum(10,12))


# 35
# def sum(x, y):
#     if x == y or x + y == 5 or abs(x - y) == 5:
#         return True
#     else:
#         return False
#
# print(sum(12,17))


