"""
Author: Noah Jett
Date: 11/12/2018
For CS:370 Algorithmic Number Theory with Professor Shallue
"Implementations" of Diffie-Hellman and RSA crypto systems
This code generates all of the values needed for those systems and simulates exchanges
Uses previously written code from this course, including trial division, prime sieve, gcd, Extended Euclidean solver, and multiplicative order
Referenced Stack overflow a couple times, cited in-line. Most notably in the generateRSA function, for handling the case when d is negative.
Variable naming and general structure is poor. Run time is substantial. Diffie-Hellman seems to compute in < 1 second. RSA varies significantly, anywhere from ~5-30 seconds.
RSA encrypts by converting to unicode, so should work for all accepted unicode characters. 
"""



import random

def main():
  g,p,n,m,gn,gm = (generateDH())
  DiffieHellman(g,p,n,m,gn,gm)

  message = "Houston, we have lift-off"

  n,p,q,e,d,phiofn = generateRSA()
  c = encrypt(message,e,n)
  mm = decrypt(c,d,n)
  finalm = "".join(mm)
  
  getmsg = attackRSA(n,e,c)
  #crackS1,crackS2 = attackDH(g,p,gn,gm)

  #print(crackS1,crackS2)
  print("Original message: ", message)
  print("Encrypted message: ", c)
  print("Decrypted message: ", finalm)
  print("Cracked msg:", getmsg)
  #print(n,p,q,e,d,phiofn)
  #print(isPrime(7))

def isPrime(n):
  if n > 1:
    for i in range(3):
      a = random.randint(2,n-1)
      if (pow(a,n-1,n) != 1):
        return False
    return True
  else:
    return False

#def attackDH(p,g,gn,gm):
  #return 1
def attackRSA(n,e,c):
  # need phiofn
  # phiofn = (p-1) (q-1), need to factor n
  a = trialDivision(n)
  p = a[0]
  q = a[1]
  phiofn = (p-1)*(q-1)
  dget = solver(e,phiofn,1)
  d = int(dget[0])
  d = d % phiofn # directly stolen from here https://crypto.stackexchange.com/questions/10805/how-does-one-deal-with-a-negative-d-in-rsa
  if(d < 0):
    d += phiofn
    
  getmsg = decrypt(c,int(d),int(n))
  crackedmsg = "".join(getmsg)
  return crackedmsg

def attackDH(g,p,gn,gm):
  n = 0
  m = 0
  for i in range(1001):
    tmp = pow(g,i,p)
    if tmp == gn:
      n = i
  for j in range(1001):
    tmp2 = pow(g,j,p)
    if tmp2 == gm:
      m = j
  return pow(gn,m,p), pow(gm,n,p)

# Generates the values used in RSA 
def generateRSA():
  p = random.randint(500,1000) # Method for picking two random primes p,q. Choose random number between 500,1000, check if prime
  q = random.randint(500,1000)
  tmp1 = isPrime(p) # My trial division function returns a list of length 1 for prime numbers
  tmp2 = isPrime(q)

  while (tmp1 == False):
    p = random.randint(500,1000)
    tmp1 = isPrime(p)

  while(tmp2 == False):
    q = random.randint(500,1000)
    tmp2 = isPrime(q)

  #while len(tmp1) > 1: # Generate random numbers until we get a prime
    #p = random.randint(500,1000)
    #tmp1 = trialDivision(p)
  
  #while len(tmp2) > 1: # probably better method than this, definitely a better way to write this code
    #q = random.randint(500,1000)
    #tmp2 = trialDivision(q)

  n = p*q
  phiofn = (p-1) * (q-1)

  e = random.randint(1,phiofn)
  # finding a random int e such that 1 < e < phiofn and gcd(e,phiofn) = 1
  check = False
  while (check == False):
    tmp3 = gcdit(e,phiofn)
    if tmp3 == 1:
      check = True
    else:
      e = random.randint(1,phiofn)
    
  dget = solver(e,phiofn,1)
  d1 = dget[0] # Referenced this article https://stackoverflow.com/questions/23279208/rsa-calculate-d
  d = int(d1)

  d = d % phiofn # directly stolen from here https://crypto.stackexchange.com/questions/10805/how-does-one-deal-with-a-negative-d-in-rsa
  # was not sure what to do when d was negative, this explained
  if(d < 0):
    d += phiofn

  return(n,p,q,e,d,phiofn)

# RSA function for converting message to unicode 
def encrypt(message,e,n):
  # Could, and probably should, have condensed these into nested for loops, or found a way to do this in place.
  # Multiple lists uses more memory. However, I like list comprehension, and like the look of this solution more
  
  m = [ord(c) for c in message] # Built in function ord() converts character to unicode. python docs
  ct = [(i**e)%n for i in m] 
  c = [int(i) for i in ct]

  return c

# RSA function for converting message from unicode to string
def decrypt(c,d,n):
  aa = [pow(i,d,n) for i in c] # Using python's built in PowerMod, since mine was actually getting incorrect values
  # Note c is in the form ["aa", "bb", "cc"] at this point.
  
  #print(aa)

  mm = [chr(j) for j in aa] # built in chr() function coverts unicode value to corresponding character. python docs
  return mm

# Generate values needed for Diffie Hellman exchange
def generateDH():
  p = random.randint(1,1000)
  tmp = trialDivision(p)
  while len(tmp) > 1:
    p = random.randint(1,1000)
    tmp = trialDivision(p)

  g = random.randint(1,p)

  n = random.randint(100,1000)
  m = random.randint(100,1000)
  if (m == n): # ensure secret keys are different
    m = random.randint(100,1000)
  gn = (g**n)%p 
  gm = (g**m)%p
  return(g,p,n,m,gn,gm)

def DiffieHellman(g,p,n,m,gn,gm):
  #print(g,p,n,m)

  #gn = PowerMod(g,n,p) Getting wrong values for some reason
  #gn = (g**n)%p 
  #gm = (g**m)%p

  s1 = (gn**m) % p
  #s1 = pow(gn,m,p)
  s2 = (gm**n) % p

  print("Publicly known, g,p,gn,gm: ", g,p,gn,gm)
  print("Privately known: My secret n, Your secret m:", n,m)
  print("Our shared secret:", s1)


"""
Below this point are helper functions, previously written code from this course
In order:
Trial division
prime sieve
binary exponentiation
gcd
multiplicative order
extended euclidean algorithm solver
"""
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

# Binary exponentiation function from earlier assignment, used in multiplicative order
def PowerMod(a,e,n): # a ** e % n
    
    #print("||", a,e,n, "||")
    if e < 1:
        #rint("Steps: ", numSteps)
        return (a)
    elif e % 2 == 0: # even case
        return (PowerMod(a, e/2, n)**2)%n
    
    elif e % 2 != 0: # odd case
        return (a * PowerMod(a, e-1, n) % n)

# Iterative GCD from earlier assignment, used in multiplicative order
def gcdit(a,b):
  while b != 0: # alternatively just while b
    gcd = b
    b = a % b
    a = gcd
  return gcd

# finds the multiplicative order of a mod n
def multiplicativeOrder(a,n):
    # Prerequisite for multiplicative order, via the textbook
    if (gcdit(a,n) != 1) : 
        return -1
  
    result = 1
  
    k = 1
    while (k < n) : 
      #print(result)     
      #result = (a ** k) % n This is one method to exponentiate, but slow
        
      result = (result * a) % n # Better method to exponentiate, by keeping a running total
      
      # result  = PowerMod(a,k,n) # best method, but was bugged 
      
      #print("result: ", result,"k: ", k)
  
      if (result == 1) : 
          return k
  
        # increment power 
      k += 1
      
    return -1

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

main()
