# Hashing nut with characters

# constraints 
#'a'<=[i]<='z'

s="azyxyyzaaaa"
q=["d","a","y","x"]
has_list=[0]*27
for ch in s :
    ascci_val=ord(ch)
    index=ascci_val-97
    has_list[index]+=1

for ch in q:
    ascci_vall=ord(ch)
    index=ascci_vall-97
    print(has_list[index])

# because of the given question we konow that only small alphabets are going to used so we came up to this logic but when all the alphabtes are considered we have to make a lager list and -97 concept also necessory

# again because we use the hashing the time complexity reduces 

#TC O(N+M)
#SC O(26) i.e O (1)
