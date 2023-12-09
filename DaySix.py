Data = open("WaitForItDaySix.txt").read().rstrip()
T, D = Data.split('\n')
_,T,  = T.split(':')
_,D,  = D.split(':')
T2 = int("".join(T.split()))
D2 = int("".join(D.split()))
T = list(map(int,T.split()))
D = list(map(int,D.split()))
res = 1
for k in range(len(T)):
    target = D[k]
    Time = T[k]
    L , R = 1,T[k]
    l1, l2 = 0, 0
    for i in range(1,Time+1):
        if i*(Time-i) > target:
            l1 = i
            break
    for j in range(R,1,-1):
        if j*(Time-j) > target:
            l2 = j+1
            break
    res *= (l2-l1)


for i in range(1,T2+1):
    if i*(T2-i) > D2:
        l1 = i
        break
for j in range(T2,1,-1):
    if j*(T2-j) > D2:
        l2 = j+1
        break
    
res2 = (l2-l1)

print(res)
print(res2)