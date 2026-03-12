import re
#

#  Regular Expression, is a sequence of characters that forms a search pattern.
# write a python program that matches a string that has a 1 followed by zero or more zeros.
# pattern=r'10*'
# print(re.search(pattern,'abc90001'))

# write a program that matches a string that has a letter followed by zero or one zero
# pattern1=r'[a-z]0?'
# print(re.search(pattern,'a00'))


# search()
# txt = "The rain in Spain"
# x = re.search("zz", txt)
# print(x)
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# # or
# string = "Hello World!"
# pattern = r"World!$"
#
# match = re.search(pattern, string)
# if match:
#     print("Match found!")
# else:
#     print("Match not found.")


# findall()

# txt = "The rain inai Spain"
# x = re.findall("ai", txt)
# print(x)

# split()
#
# txt = "The rain in Spain"
# x = re.split("in", txt)
# print(x)



# or

# txt = "The rain in Spain"
# x = re.split("\s", txt, 3)
# print(x)

# sub()
# txt = "The rain in Spain"
# x = re.sub("a", "9", txt)
# print(x)

# or
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt,2)
# print(x)

# span,string,group
#
# txt = "The rain in Spain rain"
# x = re.search("rain", txt)
# print(x)
# print(x.span())
# print(x.string)
# print(x.group())