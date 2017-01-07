import math

def outOfPie(x, y):
    return x * x + y * y > 2500

def color(n, p, x, y):
    if outOfPie(x, y):
        res = 'white'
    elif x == 50 and y == 50:
        res = 'black' if p > 0 else 'white'
    else:
        pointAngle = math.degrees(math.atan2(y, x))
        if pointAngle > 90:
            pointAngle = 450 - pointAngle
        else:
            pointAngle = 90 - pointAngle
        progressAngle = p * 360 / 100.0
        res = 'black' if pointAngle < progressAngle else 'white'
    return "Case #%d: %s\n" % (n, res)

fin = open('progress_pie.txt')
fout = open('progress_pie_output.txt', 'w')
fin.readline()
n = 1
for line in fin:
    array = line.split()
    fout.write(color(n, int(array[0]), int(array[1]) - 50, int(array[2]) - 50))
    n += 1
