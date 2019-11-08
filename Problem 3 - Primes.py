import math

###DO NOT RUN
###MEMORY ERRORS

# goal number as an integer
goal = int(input())

# create a list of primes, add every number from 2 to our goal
# goal + 1 to include the goal number
primes = []
for x in range(2, goal+1):
    primes.append(x)

# let x equal 2 as 1 is not needed
# square root the goal as an optimisation, no primes after square root factors are removed
# e.g. primes under 100 have no factors above 10.
# while x is bigger than the square of our goal, we search the list for it
x = 2
while x <= int(math.sqrt(goal)):
    if x in primes:
        # start from x * 2, then x * 3, et c, until goal is reached
        for y in range(x * 2, goal + 1, x):
            # if this number is found, remove it from the list
            # prime is never removed because only multiples are removed
            if y in primes:
                primes.remove(y)
    # increase x by 1 so next primes factors can be removed
    x = x + 1

primeFactors =[]

for z in primes:
    if goal % z == 0:
        primeFactors.append(z)

print(max(primeFactors))
