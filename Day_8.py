#@    RECURSIONS USING  PARAMETERS 


def func(x,n):
    if n==0:
        return
    print(x)
    func(x,n-1)


func(15,4)   





def func2(i,n):
    if i>n:
        return
    print(i)
    func2(i+1,n)

func2(1,4)