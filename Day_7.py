#recursion theory

# # Recursion it menas calling the function multiple times

def greet():
    print("tushar")
    greet()

greet()

# in languages like c++ and java there is thing called the stack space it keeps the record of the functions that we are calling closed it when its done.So in those languages the stack space fill"s up and we get error 

# but in python it calls the fuction for 987 times befor giving it an error 
# we have put some conditions to exit this loop

#=============================================================================================================#
count=0
def greet2():
    global count
    if count==7:
        return "stop"
    print("tushar")
    count+=1
    greet2()
greet2()

#here we can see that the function is called inside the function after the job(printing) is done so its called the head recursion 

#@ IF we call a function beforn the job is done then it is called a tail recursion

#===========================================================================================================#
i=0
def greet3():
    global i
    if i == 4:
        return print("Stop")
    
    i+=1
    greet3()
    print("Tushar")

greet3()

# here it goes to the last loop and when the condition is satisfied it returns and finishes the job below the fucntion i.e printing here 

# now lets see the TC and SC of both head and tail 

# TC = O(N+1) because the loops runs for 5 times and n is 4 
# TC =~O(N)

# SC= O(N+1) it only taks n space even in worst case scenario
# SC=~ O(N) 