from collections import defaultdict

def GearRatios():
    asteriscos = defaultdict(list)
    try:
        data = open("GearRatiosDayThree.txt")
    except:
        return
    mat = []
    line = data.readline()
    while line:
        line= line.rstrip()
        row = [line+"."]
        mat.append(row)
        line = data.readline()
    ROWS = len(mat)
    COLS = len(mat[0][0])

    suma = 0
    for i in range(len(mat)):
        item =  mat[i][0]
        curr = ""
        val = False
        gears = set()
        for j in range(len(item)):
            if item[j].isdigit():
                curr += item[j]
                for rr in [-1,0,1]:
                    for cc in [-1,0,1]:
                        if 0<= i+rr<ROWS and 0<=j+cc<COLS:
                            ch = mat[i+rr][0][j+cc]
                            if not ch.isdigit() and ch != '.':
                                if ch == '*':
                                    gears.add((i+rr,j+cc))
                                val = True
            else:
                if curr!="" and val:
                    suma += int(curr)
                    for gear in gears:
                        asteriscos[gear].append(int(curr))
                curr = ""
                val = False
                gears = set()
    pr = 0
    for key, item in asteriscos.items():
        if len(item)==2:
            pr += item[0]*item[1]
    print(pr)
    print(suma)
    return

if __name__ == "__main__":
    GearRatios()