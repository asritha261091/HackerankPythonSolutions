cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_list=[]
    if n==0:
        fib_list=[]
    if n==1:
        fib_list.append(0)
    if n>1:
        a=0
        b=1
        fib_list.append(a)
        fib_list.append(b)
        for i in range(n-2):
            x=a+b
            fib_list.append(x)
            a=b
            b=x
    return fib_list
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
