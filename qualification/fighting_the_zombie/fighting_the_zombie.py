# Fighting the Zombie
#
# For each attack, we need to compute the probability that it rolls at least H damage. We can compute this using dynamic programming.
# Let f(D, K) be the probability of dealing at least K damage with D dice. For a given input X Y Z we want to compute f(X, H - Z). We can use the following recursive definition:
# f(D, K) = 1 for K <= 0 (We can always do at least 0 damage)
# f(0, K) = 0 for K > 0 (We can't do a positive amount of damage with 0 dice)
# f(D, K) = (1 / Y) * ( f(D - 1, K - 1) + f(D - 1, K - 2) + ... + f(D - 1, K - Y) )
# This last formula combines the outcomes of all possible die rolls for a single die, and weights them evenly by 1 / Y.
# In this way, we can compute the probability of success for each attack in O(X * Y * (H - Z)) time.
# Since the most damage we can do is X * Y, we can trivially reject any case where H - Z > X * Y. That means we can also consider the time complexity to be O(X * Y * X * Y) = O(X^2 * Y^2).

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
