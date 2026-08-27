from math import sqrt


# n=10
# num=n
# list=[]
# for i in range(1,num+1):
#     if num%i==0:
#         list.append(i)
# print(list)
# #======================================================================

# n=10
# num=n
# list2=[]
# for i in range(1,num//2):
#     if num%i==0:
#         list2.append(i)
# list2.append(num)
# print(list2)

#=================================================================

n=36
num=n
list3=[]
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        list3.append(i)

        if num//i !=i:
            list3.append(num//i)

print(list3)