# frequency_map/  Dictionary

num=[1,2,3,4,54,56,7,89,1,3,4,56]

dict={}

for i in range(0,len(num)): # TC O(1)
    if num[i] in dict:# this takes TC O(1)
        dict[num[i]]+=1# TC O(1)

    else:
        dict[num[i]]=1 #TC O(1)

print(dict)