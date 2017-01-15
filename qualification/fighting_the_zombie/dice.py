from numpy.polynomial.polynomial import polypow
from numpy import ones

sides = 6
dice = 2

# Create an array of polynomial coefficients for
# x + x^2 + ... + x^sides
p = ones(sides + 1)
p[0] = 0

# Extract the coefficients of p(x)**dice and divide by sides**dice
pmf = sides**(-dice) * polypow(p, dice)
cdf = pmf.cumsum()
print cdf
