a=[5,7,-10,-3,0,3,5,1]
min=float('inf')
for i in a:
    if i>0 and i<min:
        min=i
if min==float('inf'):
    print(0)
else:
    print(min)