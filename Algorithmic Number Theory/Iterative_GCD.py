# Iterative implementation of GCD with step counter
# by Noah Jett
# For CS-370 Algorithmic Number Theory - Professor Shallue
# Followed algorithm for GCD from "Elementary Number Theory: Primes, Congruences, and Secrets" by William Stein
# No other sources
# 9/19/18

def gcdit(a,b):
    counter = 0
    # Division function: a = bq + r
    # While loop works by performing GCD division with three shifting variables
    # Keeps current gcd, the "b" and the "remainder", which we call a
    # Goes until b = 0, i.e. that the gcd has been divided equally 
    
    while b != 0: # alternatively just while b
        gcd = b
        b = a % b
        a = gcd
        counter +=1
        print(a,b,gcd)
    return gcd, counter

#print(gcdit(314159265358979323846264338,271828182845904523536028747))
print(gcdit(1638,357))
