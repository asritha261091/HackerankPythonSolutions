import numpy
n,m=map(int,input().split())
arr=[]
for _ in range(n):
    row=list(map(int,input().split()))
    arr.append(row)
np_arr= numpy.array(arr)
transp=numpy.transpose(np_arr)
flat=np_arr.flatten()
print(transp)
print(flat)
