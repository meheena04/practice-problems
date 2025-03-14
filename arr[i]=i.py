l=[-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
l.sort()
l=[i for i in l if i!=-1]
print(l)
m=l[-1]
#print(m)
res=[]
j=0
for i in range(m+1):
    if i==l[j] and j<len(l):
        res.append(i)
        j=j+1
    else:
        res.append(-1)

print(res)