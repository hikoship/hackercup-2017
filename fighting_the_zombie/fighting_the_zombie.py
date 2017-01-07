from numpy.polynomial.polynomial import polypow
from numpy import ones
import re

def probability(h, spells):
    res = 0
    for s in spells:
        data = re.split('d|\+|\-',s)
        x = int(data[0])
        y = int(data[1])
        if '+' in s:
            z = int(data[2])
        elif '-' in s:
            z = -int(data[2])
        else:
            z = 0
        realHP = h - z

        if realHP <= 0:
            return 1
        if realHP > x * y:
            continue

        p = ones(y + 1)
        p[0] = 0
        p /= y
        pmf = polypow(p, x)
        cdf = pmf.cumsum()
        res = max(res, sum(pmf[realHP:]))
    return res

def main():
    fin = open('fighting_the_zombie.txt')
    fout = open('fighting_the_zombie_output.txt', 'w')
    t = int(fin.readline())
    for i in range(t):
        h = int(fin.readline().split()[0])
        spells = fin.readline().split()
        fout.write("Case #%d: %f\n" % (i + 1, probability(h, spells)))
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()
