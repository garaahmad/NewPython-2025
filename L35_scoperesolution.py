x =10 # it Global
def func1():
    a = 1
    print(a)
    # if you want to print b in func2()
    # print(b)#ERROR IT is local
    print(x)
    
def func2():
    b = 2
    print(b)
    print(x)