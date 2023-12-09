from collections import defaultdict

D = open("IfYouGiveASeedAFertilizerDayFive.txt").read().rstrip()
lines =  D.split('\n')
_ ,seeds =  lines[0].split(':')
seeds = list(map(int,seeds.split()))
maps = defaultdict(list)
changed = False
key = "N"
for i in range(len(lines)):
    if lines[i]=='':
        changed = False
        continue
    if not changed:
        key = lines[i]
        changed = True
    else:
        values = list(map(int,lines[i].split()))
        maps[key].append(values)


locations = []
locations2 = []
for i in seeds:
    val = i
    for k, v in maps.items():
        for ran in v:
            if  val >= ran[1] and val <=  ran[1]+ran[2]:
                val = val + ran[0]-ran[1]
                break
    locations.append(val)

for i in range(0,len(seeds),2):
    S = seeds[i]
    E = seeds[i]+seeds[i+1]
    for s in range(S,E):
        val = s
        for k, v in maps.items():
            for ran in v:
                if  val >= ran[1] and val <=  ran[1]+ran[2]:
                    val = val + ran[0]-ran[1]
                    break
        locations2.append(val)


print(min(locations))
print(min(locations2))
   

