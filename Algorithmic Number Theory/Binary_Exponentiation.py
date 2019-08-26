# Author: Noah Jett
# Date: 10/1/2018
# CS 370: Algorithmic Number Theory  - Prof. Shallue
# This program is an implementation of the binary exponentiation algorithm to solve a problem of form a**e % n in fewer steps
# I referenced our classroom discussion and the python wiki for the Math.log2 method

import math
def main():
    a,n = 2,3
    for e in range(1,10):
        print("e ==: ", e)
        result = (PowerMod(a,e,n,1))
        print("Answer: ", result)
        logTest = logbase2(e)
        print("2 * log base2(e) = ", logTest, "\n")
    
def PowerMod(a,e,n,numSteps): # a ** e % n
    
    print("||", a,e,n, "||")
    if e < 1:
        print("Steps: ", numSteps)
        return (a)
    elif e % 2 == 0: # even case
        return (PowerMod(a, e/2, n, numSteps+1)**2)%n

    elif e % 2 != 0: # odd case
        return (a * PowerMod(a, e-1, n,numSteps+1) % n)

# Takes input e, the exponent being calculated in powermod
# Outputs 2*log base2(e)
# I googled "python log base 2" library, and was directed (stackoverflow?) to the log2 function in the "math" library
def logbase2(e): 
    log = (math.log2(e))*2
    return log

main()

"""
 This algorithm for binary exponentiation should theoretically take <= logbase2(e) *2 steps to solve.
 I tested this for exponents 1-100 for the equation 2**e % 3.
 The algorithm did not consistently take <= 2logbase2(e) steps until the exponent was >= 16. With the exceptions of 31 and 63
 The exponents that solved in the least steps, around 25% fewer than 2logbase2(e) were:
 16,24,32,34,36,48,64,72... There was a positive correlation between even numbers and fewer steps, and an even greater one between powers of 2 and fewer steps.
 Some exponents that took more steps, being only slightly better than the theoretical limit were:
 19,21,23,31,47,79,95. Odd numbers and primes both seem to take more steps to solve

 Why is this the case?
 The first fifteen exponents exceed the theoretical upper bound. I suspect this is overhead from python or my specific code.
 However, it also makes sense that this algorithm will always take at least a few steps, so it might just not work under a certain number.
 It makes sense that odd numbers would be slightly slower. Algorithmically, the odd case is essentially the # of even stepe +1
 Powers of 2 being faster probably has to do with having a base of 2; those numbers would divide perfectly. 

"""

