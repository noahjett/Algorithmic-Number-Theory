'''
Author: Noah Jett
Date: 9/19/2018
Implementation of Eratosthenes sieve and trial division in python
For CS:370 Algorithmic Number Theory with Andrew Shallue

'''
import time

# Inputs: Takes arguments for: The primes up to [n], the factors of [n], the factors of every number up to [n]
# Outputs the prime numbers of up to Input 1, the factors of input 2, and every number up to input 3 and that numbers factors
# Also outputs runtimes for every function
# Note: The whitespace and variable naming in this code are pretty bad, I did not have time to clean it up

def main():

    # These code blocks query for an input, run a function on that query and record the time that function call takes

    a = eval(input("Give me the primes up to...!: "))
    sieveStart = time.time()
    print(sieve(a))
    sieveEnd = time.time()
    sieveTotal = sieveEnd - sieveStart
    
    b = eval(input("Give me the factors of...!: "))
    trialStart = time.time()
    print(factors_of(b))
    trialEnd = time.time()
    trialTotal = trialEnd - trialStart

    divideStart = time.time()
    print(trialDivision(b))
    divideEnd = time.time()
    divideTotal = divideEnd - divideStart
    
    c = eval(input("Give me the factors of every number up to...!: "))
    NaivefactorStart = time.time()
    factors_uptoNaive(c)
    NaivefactorEnd = time.time()
    NaivefactorTotal = NaivefactorEnd - NaivefactorStart

    BetterFactorStart = time.time()
    factors_uptoBetter(c)
    BetterFactorEnd = time.time()
    BetterFactorTotal = BetterFactorEnd - BetterFactorStart

    print("Runtimes for \n Sieve: %s \n Naive Trial Division: %s \n Better Trial Division: %s \n Naive Factors up to: %s \n Better Factor up to: %s \n Naive Total time: %s \n Better Total Time: %s" %(sieveTotal, trialTotal, divideTotal, NaivefactorTotal, BetterFactorTotal, sieveTotal + trialTotal + NaivefactorTotal, sieveTotal + divideTotal + BetterFactorTotal))

    print("GCD of 314159265358979323846264338,271828182845904523536028747", gcdit(314159265358979323846264338,271828182845904523536028747))
    
# Implementation of Erthemolastrepes Sieve
# Input: An integer upper bound n
# Output: The prime numbers up to n
# At first I looked at algorithm on wikipedia, but classwork is what helped me figure this out
# Reading through Python docs I found the "not in" expression, https://docs.python.org/3.7/reference/expressions.html,
# and found it very useful. I kept two lists because I thought that expression simplified the code a lot, and helped my understanding

def sieve(n):
    not_prime = [] # Instantiate two lists
    prime = []
    
    #print(not_prime, prime) debug, these are helpful for showing how it works
    
    for i in range(2,n+1): # For all the numbers > 2 to our upper limit
        #print(i)
        
        if i not in not_prime: # i is our factor; if it isn't not prime, it is prime; works because we start with 2
            prime.append(i)
            #print(prime)
            
            for j in range(i*i, n+1, i): # Divide through our range by increments of our factor, i, adding them to not prime
                not_prime.append(j)
                #print(not_prime,prime) 
                
    #print(not_prime,prime)
    return prime

# This is Wikipedia's Implementation of Trial division: I DID NOT WRITE THIS
# Found at https://en.wikipedia.org/wiki/Trial_division by Unknown Author
# Used to help understand the inner workings of the sieve
# Also is less than optimal because it divides by every number between 2 and n, rather than just the primes
# Used in testing to see if it is less efficient

def factors_of(n): 
    listy = []
    factor = 2 
    while n > 1:
        #print(n,factor,listy) Shows state of variables
        if (n % factor == 0):
            listy.append(factor)
            n = n/factor
        else:
            #print(factor, "does not divide", n) #Debug, shows why the factor is incremented
            factor += 1
    return listy


# My implementation of trial division, considering our class discussion
# We only need to "divide" by the primes, and we can divide by incrementing by the prime in a for loop
# Also, only need to consider primes up to sqrt(n), for reasons discussed in class

def trialDivision(n):
    if n ==1: 
        return 1
    
    primes = sieve(int(n**0.5)+1) # Making use of our sieve to get the primes up to sqrt(n)
    factors = []

    #print(primes,factors) # debug

    for i in primes: # For each prime,
        
        if i*i > n: # if prime^2 > n, then we do not need to consider it
            break # I generally avoid break, easiest solution here

        # "While" instead of "if", because a prime factorization can have the same factor twice
        # If n is prime, this while loop will append nothing
        while n % i == 0: # while n is evenly divided by i
            
            #print(n,i,factors) # debug
            factors.append(i) #add i to factors
            n /= i # Divide base by factor EX.) 50 % 2 == 0, factors.append(2), 50/2 = 25
            #print("a", n, "%", i,factors) #debug
            
        # If factored, n == 1, after this loop

    # If n !=1 at this point, it has not been factored, and is therefore prime        
    if n > 1: 
        factors.append(n)
    return factors


# This calls Wikipedia's trial division function on every # up to n
def factors_uptoNaive(n):
    for i in range(0, n+1):
        print(i, factors_of(i))

# This calls my trial division function on every # up to n
def factors_uptoBetter(n):
    for i in range(0, n+1):
        print(i, trialDivision(i))


# Iterative implementation of GCD with step counter
# To show problem 1.11 B from the book
# Followed algorithm for GCD from "Elementary Number Theory: Primes, Congruences, and Secrets" by William Stein
# No other sources

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
    return gcd, counter

main()

