# Recursive implementation of GCD with step counter
# by Noah Jett
# For CS-370 Algorithmic Number Theory - Professor Shallue
# Followed algorithm for GCD from "Elementary Number Theory: Primes, Congruences, and Secrets" by William Stein
# Considered Evan's algorithm from class
# 9/12/18

def gcd_rec(a,b, numsteps):
  # Note that numsteps should be passed as 1 if you want the first step to be counted

  
  if b: # alternatively while b != 0
    print(a,b)
    return gcd_rec(b,a%b, numsteps + 1)
  else:
    print(a,b)
    return a, numsteps

print(gcd_rec(1638,357,1))
