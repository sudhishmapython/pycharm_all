# Right Half Pyramid Pattern

# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()


# left half
# rows = int(input("Enter the number of rows: "))
# for i in range(1, rows + 1):
#     for j in range(1, rows + 1):
#         if j <= rows - i:
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     print()


# full
# for i in range(5):
#   for j in range(5-i):
#     print(' ', end = " ")
#   for k in range(i+1):
#     print("*",end = "   ")
#   print()



# reverse right half
# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i ,n):
#         print("*", end=" ")
#     print()



# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print("")


# for i in range(1,6):
#     for j in range(1,i):
#         print(j,end=" ")
#     print("")






# largest number
# a = [10, 24, 76, 23, 12]
# largest = a[0]
# for val in a:
#     if val > largest:
#         largest = val
# print(largest)


# fibinacci series

# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# factorial
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial of", num, "is", factorial)


# prime number

# num = int(input("Enter a number: "))
# prime_num = 0
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             prime_num = 1
#             break
# else:
#     prime_num = 1
#
# if prime_num==0:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")
