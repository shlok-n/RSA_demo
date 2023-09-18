#============================================#
def isPrime(x):
    count = 0
    for i in range(2, int(x/2)):
        if x%i==0:
            return False
    return True

#============================================#


#============================================#
def isCoprime(i, phi):
    
    factors = [] 
    for factor in range (2,int(phi/2)+1):
        if phi%factor == 0:
            if factor <= i:
                factors.append(factor)
    
    
    for value in factors:
        if i%value == 0:
            return False
    
    return True
#============================================#


#============================================#
def encrypt(public_key, msg):
    e = public_key[0]
    n = public_key[1]
    c = (pow(msg,e))%n
    return c
#===========================================#


#============================================#
def decrypt(private_key, enc_msg):
    d = private_key[0]
    n = private_key[1]
    m = (pow(enc_msg,d))%n
    return m
#============================================#


minPrime = 1033
maxPrime = 6091
cached_primes = [i for i in range(minPrime,maxPrime) if isPrime(i)==True]

import random

p = random.choice(cached_primes)
q = random.choice(cached_primes)
e = None
n = p*q
phi = ((p-1)*(q-1))
d = None

for i in range (2,n):
    if  isCoprime(i, phi) == True:
        e = i
        break
        
public_key = [e,n]

i = 1
while(i):
    if (e*i)%phi == 1:
        d = i
        break
    else:
        i+=1
        
private_key = [d,n]

print()
print("p :"+str(p))
print("q :"+str(q))
print("n :"+str(n))
print("phi :"+str(phi))
print("e :"+str(e))
print("d :"+str(d))
print("public_key :"+str(public_key))
print("private_key :"+str(private_key))
print()
msg = int(input("Enter your message (integer only): "))

Encrypted_msg = encrypt(public_key, msg)
print("Encrypted_msg :"+str(Encrypted_msg))

Decrypted_msg = decrypt(private_key, Encrypted_msg)
print("Decrypted_msg :"+str(Decrypted_msg))
print("\n")