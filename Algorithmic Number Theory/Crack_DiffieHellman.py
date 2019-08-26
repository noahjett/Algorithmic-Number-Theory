"""
Author: Noah Jett
Date: 11/4/2018
For CS 370 Algorithmic Number Theory - Professor Shallue

Python code cracking a naive Diffie-Hellman key exchange
Referenced "Elementary Number Theory" By William Stein

Uses my previously written code to find the gcd, and solve extended euclidean problems in the "gcdit" and "solver" functions respectively
"""

# This follows the algorithm on page 51 of the textbook
def crack(p,g,ng,mg):
    a,b = solver(g,p,1) # Solve equation ag + bp = 1 for some numbers a,b with extended euclidean
    n = (a*ng) % p # We know a*ng is congruent to n(mod p), so we can easily solve for n
    s = n * mg % p # Solve for secret with private n, and publically known mg
    print(s)


    
def gcdit(a,b):
    while b != 0: # alternatively just while b
        gcd = b
        b = a % b
        a = gcd
    return gcd

def solver(a,b,c):

    # solve for integer quotient q, and remainder r
    q = a // b
    r = a % b

    #print("a = ",a,"b = ", b,"c = ", c) debug
    #print("a // b, q, = ", q) 
    #print("a % b, r,  = ", r)

    if r == 0:
        check = gcdit(a,b)
        if c % check != 0:
            return "No solution"
        else:
            return([0,c/b])
    else:
        # print(a,b,c,q,r)
        
        listy = solver(b,r,c)
        m = listy[0]
        n = listy[1]
        
        # print("m",m,"n",n,q)
        return([n, m - q*n])


crack(97,5,58,87)
    
