# f=open('bio.txt','r')
# data=f.read()
# print(data)
# print('File Read successfully')
# f.close()


# f=open('bio.txt','r')
# data=f.readlines(1)
# print(data)
# print('File Read successfully')
# f.close()



# f=open('bio1.txt','w')
# lst=['Hello,World!\n','This is a second line']
# f.writelines(lst)
# f.close()
# f=open('bio1.txt','r')
# data=f.read()
# print(data)
# print('File Read successfully')
# #f.close()
# print(f.name)
# print(f.mode)
# print(f.closed)
# print(f.readable())


# with open('bio.txt','r') as f:
#     data=f.read()
#     print(data)
# print("File closed: ",f.closed)

# with open('bio.txt','rb') as f:
#     f.seek(15,0)
#     p=f.tell()
#     print(p)
#     data=f.read(50)
#     print(data)



# import os
# # os.rename("bio.txt","bio2.txt")
# os.remove("display.py")  

f=open("morgan.jpg",'rb')
img=f.read()
print(img)