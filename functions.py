import random

def setseed(s:int):
    random.seed(s)

def rabinMiller(num):
   s = num - 1
   t = 0
   
   while s % 2 == 0:
      s = s // 2
      t += 1
   for trials in range(5):
      a = random.randrange(2, num - 1)
      v = pow(a, s, num)
      if v != 1:
         i = 0
         while v != (num - 1):
            if i == t - 1:
               return False
            else:
               i = i + 1
               v = (v ** 2) % num
      return True
    

def phi(n):
    if n == 0:
        return 1
    out = 0
    for i in range(1, n):
        if ggT(n, i) == 1:
            out += 1
    return out

def ggT(n1, n2):
    while n2 != 0:
        if n1 > n2:
            n1 -= n2
        else:
            n2 -= n1
    return n1

def gcd(a, b):
   while a != 0:
      a, b = b % a, a
   return b

def isprime(n):
    if n > 1:
        for i in range(2, n):
            if n%i == 0:
                return False
    return True

def isPrime(num):
   if (num < 2):
      return False
   lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
   67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
   157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
   251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,317, 331, 337, 347, 349, 
   353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 
   457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 
   571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 
   673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
   797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 
   911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
	
   if num in lowPrimes:
      return True
   for prime in lowPrimes:
      if num % prime == 0:
         return False
   return rabinMiller(num)

def highprime(size=1024):
    while True:
        n = random.randint(2**(size-1), 2**size)
        if isPrime(n):
           return n

def ModInverse(e, phin):
    if gcd(e, phin) != 1:
        return None
    u1, u2, u3 = 1, 0, e
    v1, v2, v3 = 0, 1, phin
    
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % phin
    
def createkeys(size=1024):
    p = highprime(size)
    q = highprime(size)
    n = p*q
    e = 0
    phin = (p-1)*(q-1)
    while not (gcd(e, phin) == 1):
        e = random.randrange(2 ** (size - 1), 2 ** size)
    d = ModInverse(e, phin)
    #public: (d, n)
    #private: (e, n)
    return p, q, n, e, d

def encode(d, n, m):
    return pow(m, d, n)

def decode(e, n, c):
    return pow(c, e, n)
