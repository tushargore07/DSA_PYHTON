#      ********** HASHING **************
#prestorig values into some datastructure like lists/Dictionary / sets and the fetching it 


n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]

# 1) 1<=n[i]<=10
# 2) n can have 10**8
# 3) m can have 10**8

# we just need to tell how many times times the elements in m are there in n
#@ how manay times 10 appear in n list 

#****************Basic/brute force solution **************

for num in m:
    count=0
    for num2 in n:
        if num2==num:
            count+=1

    print(count)


# HERE TC= O(n*m)
# which is higher because (10**8X 10**8== 10**16) question want TC upto 10***


#***************** Optimal solution***********

has_list=[0]*11
for num3 in n :
    has_list[num3]+=1

for num4 in m:
    if num4<1 or num4>10:
        print(0)

    else:
        print(has_list[num4])



# here the TC is 0(m+n) which is ( 10**8+10**8=  2*10***)

# the finale TC is (~10**8) THIS IS CALLED HASHING  