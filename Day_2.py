#ARMSTRONG NUMBER 

n=int(input("Enter the number"))
num=n
nod=len(str(n))
total=0
while num>0:
    ld=num%10
    sq=ld**nod
    total=total+sq 
    num=num//10



