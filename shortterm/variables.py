
# variable declaration
# x = 5
# y = "John"
# print(x)
# print(y)

# type
# x = 5
# print(type(5))


# name=input("enter your name:")
# print(type(name))

# num1=1
# num2=2
# num3=num1+num2

# print("result is",num3)
# print(f"result is {num3}")
# print("result is",num3)


# formatted string
# print(f"result is {num3}")


# variable casting
# x = str(3)
# y = int(3)
# z = float(3)
# print(type(x))

# eg:
# name1=int(input("enter your age:"))
# print(type(name1))



# def count_words_in_file(filename):
#     import string
#
#     # Initialize an empty dictionary to hold word counts
#     word_counts = {}
#
#     # Open the file for reading
#     with open(filename, 'r') as file:
#         # Read the file line by line
#         for line in file:
#             # Remove punctuation and convert to lowercase
#             line = line.translate(str.maketrans('', '', string.punctuation)).lower()
#             # Split the line into words
#             words = line.split()
#
#             # Count each word
#             for word in words:
#                 if word in word_counts:
#                     word_counts[word] += 1
#                 else:
#                     word_counts[word] = 1
#
#     return word_counts
#
#
# # Example usage:
# filename = 'abc.txt'  # Replace with the path to your text file
# word_counts = count_words_in_file(filename)
# print(word_counts)



#
# abc=100
# def sum():
#     global name
#     name="abc"
#     print(name)
#
#
# sum()
#
# print(name)




# num1=1
# num2=2
# num3=num1+num2

# print("result is",num3)
# print(f"result is {num3}")






# xor swap

# a = 5 → binary: 0101
# b = 3 → binary: 0011



# XOR (exclusive OR) rules:
#
# 0 ^ 0 = 0
#
# 1 ^ 0 = 1
#
# 0 ^ 1 = 1
#
# 1 ^ 1 = 0


# a = 0101(5)
# ^ b = 0011(3)
# ------------
# 0110(6)


# step 2
# a = 0110(6)
# ^ b = 0011(3)
# ------------
# 0101(5)


# step3

# a = 0110(6)
# ^ b = 0101(5)
# ------------
# 0011(3)


# a = 3 (original b)
#
# b = 5 (original a)