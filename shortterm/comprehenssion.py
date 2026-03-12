# odd/even
list1=[1,3,2,4,6,7,34,23]
# even_num=[]
# for i in list1:
#     if i%2==0:
#         even_num.append(i)
# print(even_num)

[2,'long',6,'']

even=[i**2 for i in list1 if i%2==0]
print(even)




# even=[i+2 for i in list1 if i%2==0]
# print(even)

# even=[i+10 for i in list1 if i%2==0]
# print(even)



# even=[i+2 for i in list1 if i%2==0]
# print(even)



#
# even=[i**2 for i in list1 if i%2==0]
# print(even)



# even=[i*2 for i in list1 if i%2==0]
# print(even)

# even_num=[i for i in list1 if i%2==0]
# print(even_num)


# org_list=list(range(1,20+1))
# even_list=[]
# for item in org_list:
#     if item%2==0:
#         even_list.append(item)
# print(org_list)
# print(even_list)

# org_list=list(range(1,20+1))
# even_list=[item*3 for item in org_list if item%2==0 ]
# print(even_list)



# palindrom
# list2=['malayalam','english','mom','hindi','abbba']
#
#
# list1=[]
# for i in list2:
#     if i==i[::-1]:
#         list1.append(i)
# print(list1)


# # using list comprehension
# list1 = ['malayalam', 'english', 'mom', 'hindi', 'abbba']
# list2 = [i for i in list1 if i == i[::-1]]
# print(list2)



# list comprehsn(tasks)
# palindrom (integers)

# list3 = [121, 232, 464, 472]
# list4 = [i for i in list3 if str(i) == str(i)[::-1]]
# print(list4)


# 1
# list2=[input("enter a number") for i in range(4)]
# print(list2)


# 2
#
# lst1=[2, 4, 6, 8, 10, 12, 14]
# lst2 = [i**2 for i in lst1]
# print(lst2)



# 3
# demolist=[1,5,2,8,54,76,12,68,69]
# list3=[i for i in demolist if i%2!=0]
# print(list3)


# 4
# demolist1=[1,2,3,4]
# string1="abc"
# list4=[(i,j) for i in demolist1 for j in string1]
# print(list4)




# set comprehesn
# 1
# setdemo={1,5,4,7,6,4,8,1,1}
# set1={i for i in setdemo}
# print(set1)

# 2

# dictionary comprhsn
# 1


#
# dic1={i:i+2 for  i in range(1,11) }
# print(dic1)





# dicdemo={"anu":25,"abhi":30,"akhil":28}












# dic={i.upper():j for i,j in dicdemo.items()}
# print(dic)




# 2
# dicdemo={"anu":25,"abhi":30,"akhil":28}
# #
# dic2={k.upper():v for k,v in dicdemo.items()}
# print(dic2)






# 3 get keys only
# dicdemo={"anu":25,"abhi":30,"akhil":28}
# dic3={k.upper():k for k in dicdemo.keys()}
# dic4={k.upper():k for k in dicdemo.keys()}
# print(dic3)





# 4 gnerator comprhsn
# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
# output_gen = (i for i in input_list if i % 2 == 0)
# print(output_gen)
# for i in output_gen:
#     print(i)


