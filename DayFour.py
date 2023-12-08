D = open("ScratchcardsDayFour.txt").read().rstrip()
lines = D.split('\n')
total = 0
L = len(lines)
copies = [1 for i in range(L)]
for l in range(L):
    _ , data = lines[l].split(':')
    w , p = data.split('|')
    w = list(map(int,w.split()))
    p = list(map(int,p.split()))
    points = 0
    multi = 2
    cards = 0
    for num in p:
        if num in w:
            cards += 1
            if points>0:
                points = points * multi
            else:
                points = 1

    for i in range(cards):
        if i>=L:
            break
        ind = l+i+1
        copies[ind]+=copies[l]
    total += points
suma = 0
for item in copies:
    suma += item
print(total)
print(suma)


