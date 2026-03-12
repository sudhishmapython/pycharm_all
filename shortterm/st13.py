
# all factors of a number
# num = int(input('enter the number'))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i,end=",")

# check armstrong numbers

# '153'

# num = input('enter the number')
# sum=0
#
# for i in num:
#     sum+=int(i)**len(num)
#
# if sum==int(num):
#     print('armstrong')
# else:
#     print('not armstrong')

# 8208, 9474, 54748





## Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# a+aa+aaa+aaaa
# num = '9'
# sum=0
# for i in range(1,5):
#     sum+=int(num*i)
# print(sum)











#########################################################
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# s ='Hello World!'
# upper =0
# lower = 0
# for i in s:
#     if i.isupper():
#         upper+=1
#     if i.islower():
#         lower+=1
#
# print("upper:",upper)
# print("lower:",lower)


# ### special characters
# s='@#hell#o@123% wo#r@ld@'
# count1 =0
# count2=0
# for i in s:
#     if i=='@':
#         count1+=1
#     if i=='#':
#         count2+=1
#
# print(count1,count2)

#########################################
# string = input('enter the string')
# count1=0
# count2=0
# for i in string:
#     if i.isalpha():
#         count1+=1
#     if i.isdigit():
#         count2+=1
# print(count1,count2)












################################################################3
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# pattern printing

# 1.
# rows = int(input("Enter number of rows: "))
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print("\n")

# 2.
# for i in range(1,6):
#     var = 2
#     for j in range(i):
#         print(var,end=' ')
#         var**=2
#     print()
# 3.
# rows = 5
# # # reverse loop
# for i in range(rows, 0, -1):
#     num = i
#     for j in range(0, i):
#         print(num, end=' ')
#     print("")

#4.
# l = [1,5,7]
# if not l:
#   print("List is empty")
# else:
#     print("list element exist")


# Initialize the previous number to 0
previous_num = 0

print("Current Number | Previous Number | Sum")
for current_num in range(1,11):
    sum_nums = current_num + previous_num
    print(f"{current_num:^14}|{previous_num:^17}|{sum_nums:^5}")
    previous_num = current_num


