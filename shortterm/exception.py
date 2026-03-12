# x=1
# y=2
#
# try:
#     z=x/y
#     print(m)
# except ZeroDivisionError:
#     print("Zero division")
#
# except TypeError:
#     print("type error")
#
# except Exception as e:
#     print(e)
# finally:
#     print("finlly block")



#
# try:
#     z=x/y
#     print("the value is",z)
# except ZeroDivisionError:
#     d="zero not allowed"
#     print(d)
# except NameError:
#         print("the above error is name error")
# except Exception as e:
#          print("error",e)
# else:
#     print("correct it")
# finally:
#                 print("have a good day!")
#


#
# #
# try:
#     x = int(input("Enter the first number: "))
#     y = int(input("Enter the second number: "))
#
#     try:
#         z = x / y
#         print(z)
#     except ZeroDivisionError:
#         print("Zero division error occurred")
#     except NameError:
#         print("Name error occurred")
#     except ValueError:
#         print("Invalid input. Please enter valid integers.")
#     except Exception as e:
#         print("Exception occurred:", e)
#     else:
#         print("No exception")
#     finally:
#         print("Final block")
# except ValueError:
#     print("Invalid input. Please enter valid integers.")


# filename = "abc.txt"
#
# try:
#     try:
#         file = open(filename, "r")
#         print("File opened successfully.")
#
#         try:
#             # Read only the FIRST line
#             line = file.readline().strip()
#             number = int(line)
#             print("Number in file:", number)
#
#         except ValueError:
#             print("Error: The first line is not a valid integer.")
#
#         finally:
#             file.close()
#
#     except FileNotFoundError:
#         print("Error: File not found!")
#
# except Exception as e:
#     print("Unexpected error:", e)
#
#


# raise an error
# x=1
# y=2
# #
# if x<5:
#     raise Exception("futura error")
# else:
#     print(x)