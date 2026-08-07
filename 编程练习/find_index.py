a=[1,8,77,96,57]
b=77
c=88
def find(x,n):
    for i in range(len(x)):
        if x[i]==n:
            print(i)
            return i
    return -1
find(a,c)


