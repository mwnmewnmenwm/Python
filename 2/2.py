#1
from itertools import *
c = 0
for i in product('КАТЕР', repeat=6):
    if  i[0]=='Р' and i[-1]=='К':
        c += 1
print(c)


#2
x = 216 ** 6 + 216 ** 4 + 36 ** 6 - 6 ** 14 - 24
A=[]
while x>0:
    A.append (x%6)
    x//=6
print (len(set(A)))


#3
for i in range(123450708,123459799):
    if (i%23==0) and (i%10==8) and ((i//100)%10==7):
        print(i, i//23)
