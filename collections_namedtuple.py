from collections import namedtuple
n,ind=int(input()),(input().split())#.index('MARKS','CLASS','ID','NAME')
values = [];x = {}
print(ind)
for i in range(n):
   values.append(input().split())

  
print(values)


print()
print(50*'+')
print()

for i in range(len(ind)):
    a =[]
    for j in range(len(values)):
        a.append(values[j][i])
    x[ind[i]] = a
        
        
print(x)



input:
TESTCASE 01
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
TESTCASE 02
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
