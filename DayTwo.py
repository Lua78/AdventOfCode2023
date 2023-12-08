from collections import defaultdict
def CubeConundrum():
    try:
        data = open("CubeConundrumDayTwo.txt")
    except:
        print("Ups, error al intentar abrir el archivo")
    reg = data.readline()
    limits = {"green":13,"red":12,"blue":14}
    suma = 0
    while reg:
        colors = defaultdict(int)
        flag = True
        datos = reg.split(':')
        id = datos[0]
        _, id = id.split()
        id = int(id)
        datos = datos[1].split(';')
        for item in datos:
            elements = item.split(',')
            for elem in elements:
                count , color = elem.split()
                colors[color] = max(colors[color],int(count))
                if limits[color]<int(count):
                    flag = False
        score = 1
        for val in colors.values():
            score *= val
        print(score)
        suma += score
        
        reg = data.readline()
    print(suma)
if __name__ == "__main__":
    CubeConundrum()