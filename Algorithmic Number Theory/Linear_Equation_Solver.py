'''
Author: Noah Jett
Date: 10/8/2018
CS:370 - Algorithmic Number Theory with Professor Shallue
This python code solves linear diophantine equations of the form ax + by = c, solving for x,y

This code takes 3 inputs a,b,c and outputs a list of 2 values [x,y], it solves recursively

The algorithm for this code is based on the Euclidean algorithms, and my own algebraic observations

The base case is based on an observation I made looking at our class notes:
That is that if b divides a, then we can say x = 0 and y = c/b
Example, 4x + 2y = 8. x = 0, y = 4. This means we have a trivial solution in any case where b%a == 0

The main solving portion, in the ELSE, is based on the Euclidean algorithm
We consider the division formula a = bq + r
We can substitute this into our main equation to get:  (bq+r)x + by = c
Simplify to:  bqx + by + rx --> b(qx+y) + r(x)= c
I used variables m = (qx+y) and n = (x), simplifying our eqution to b(m) + r(n) = c
If we solve the m and n expressions for x,y, we get x = n, y = m-qn

SO, we run the euclidean algorithm recursively on our inputs until we get r = 0, which returns b,r,c to our last recursive call
This call takes b,r as m,n, and solves for x,y with the above expressions

Citations:
Stein, William A. Elementary Number Theory: Primes, Congruences, and Secrets. Springer, 2009.
Wikipedia contributors. "Diophantine equation." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 22 Aug. 2018. Web. 9 Oct. 2018.

'''
# Code to solve linear diophantine equation

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


print(solver(4,2,41))
print(solver(97,35,13))


