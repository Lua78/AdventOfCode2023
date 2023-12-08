
def santaFloor(steps):
    res = 0
    for i in range(len(steps)):
        if steps[i]=='(':
            res += 1
        elif steps[i] == ')':
            res -=1
        if res == -1:
            return i+1
    return res 

def calibrationValues():
    nums = {"one":"1","two":"2","three":"3","four":"4" ,"five":"5","six":"6","seven":"7","eight":"8","nine":"9","zero":"0"}
    try:
        data = open("CalibrationValuesDayOne.txt")
    except:
        print("Ups, no se ha podido abir el archivo...")
        return
    
    line = data.readline()
    sum = 0
    count = 0
    while line:
        f , l = None , None
        tam = len(line)
        curr = None
        count +=1
        for i in range(tam):
           
            if line[i].isdigit():
                curr = line[i]
            elif i<=tam-4 and line[i:i+4] in nums:
                curr = nums[line[i:i+4]]
            elif i<=tam-3 and line[i:i+3] in nums:
                curr = nums[line[i:i+3]]
            elif i<=tam-5 and line[i:i+5] in nums:
                curr = nums[line[i:i+5]]
            if curr!=None:
                if f == None:
                    f=curr
                else:
                    l = curr 
                curr = None
        if l == None:
            l = f
        sum += int(f+l)
        line = data.readline()
    data.close()
    print(sum)

if __name__ == "__main__":
    calibrationValues()

