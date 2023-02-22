n= int(input())
lst=[]
res=[]
dct={}
for i in range(n):
    lst.append(int(input()))

for k in lst:
    dct[k]=lst.count(k)
#как???
for k, v in dct:
    if dct[k]>1:
        res.append(dct[v])

print(res)