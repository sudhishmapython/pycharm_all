import csv


file=open(r'C:\Users\user\Desktop\student_marks.csv','r')
content=csv.DictReader(file)
for i in content:
    print(i['Student Name'])


file.close()





details=[
    ['Name','Mark','Rollno'],
    ['Anu',85,10],
    ['Sonu',95,12]
]
#
#
with open(r'C:\Users\user\Desktop\student_marks1.csv','w',newline="") as file:
    data=csv.writer(file)
    data.writerow(details[0])
    # data.writerows(details)


















# read
# file=open(r'C:\Users\LENOVO 10\Desktop\file.txt','r')
# x=file.readlines()
# print(x)

# print(file.read(5))
# print(file.read(6))
# print(file.readline())
# print(file.readlines())
# file.close()


# write
# file=open(r'C:\Users\user\Desktop\demo1.txt','w')
# file.write("futura calicut\n")
# file.writelines(['data1','\ndata2'])
# file.close()

# file=open('python.txt','a')
# file.write("\npython\n")
# file.close()
# or
# file=open(r'C:\Users\LENOVO 10\Desktop\file3.txt','a')
# file.close()


# x mode(new file create only)
#
# file=open("abcd.txt",'x')
# file.close()


# r+ mode
# file=open('demo.txt','r+')
# content = file.read()
# print(content)
# file.write('\nAppending new content')
#
# file.close()
# # or
# file=open(r'C:\Users\LENOVO 10\Desktop\file.txt','r+')
# content = file.read()
# print(content)
# file.close()

#delete
# import os
# os.remove('demo.txt')














# 1.write()


# file2=open("demo1.txt","w")
# file1=open("python.txt","w")
# file2.write("sudhishma\n")
# file2.write("shahala")
# file1.write("append1\n")
# file1.close()
# file2.close()


# file=open("abc.txt",'w')
# file.write("data1\n")
# file.write("data2\n")
# file.close()
# 2.read()
# file=open("demo.txt.txt",'r')
# print(file.read())
# print(file.read(5))
# print(file.readline())
# file content as list
# print(file.readlines())
# for i in file:
#     print(i)
# file.close()
# 3.append()
# file=open("demo.txt.txt",'a')
# file.write("data3\n")
# file.write("data4\n")
# file=open("demo.txt.txt",'r')
# print(file.read())
# file.close()





# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)
# File is automatically closed here


# with open("demo.txt", "r+") as f:
#     f.write("HELLO")       # overwrites from start
#     f.seek(0)
#     data = f.read()        # reads after written content
#     print(data)




# word file
# pip install python-docx


# from docx import Document
#
# doc = Document("doc.docx")
# for para in doc.paragraphs:
#     print(para.text)
