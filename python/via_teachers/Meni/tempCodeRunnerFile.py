lst=[]
k=1
step=1
for i in range(6):
    row=[]
    for j in range(6):
            row.append(k)
            k+=step
    step*=-1
    k+=step
    lst.append(row)
print(lst)

for row in lst:
    print(*row)