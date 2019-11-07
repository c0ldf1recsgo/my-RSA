'''
    *** TP HCM, 2019 ***
    Build RSA randomly
    Created by : Shayne Johnson
    - Lambda = 64
'''

import time
import math
import random

_lambda = 64

# TODO: Tim uoc chung lon nhat cua hai so a, b
def GCD(a, b):
    if (b == 0):
        return a
    return GCD(b, a % b)



# TODO: Kiem tra xem mot so co phai so nguyen to hay khong
# fast prime check for large number
def is_prime(n, k=128):
    if (n == 2 or n == 3):
        return True
    if (n <= 1 or n % 2 == 0):
        return False

    s = 0
    r = n - 1
    while (r & 1 == 0):
        s += 1
        r //= 2
        
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, r, n)
        if (x != 1 and x != n - 1):
            j = 1
            while (j < s and x != n - 1):
                x = pow(x, 2, n)
                if (x == 1):
                    return False
                j += 1
            if (x != n - 1):
                return False
    return True



# TODO: Tao hai so nguyen to p, q
def prime_gen():
    p = random.randrange(pow(2, _lambda/2 - 1), pow(2, _lambda/2))
    while (is_prime(p) == False):
        p = random.randrange(pow(2, _lambda/2 - 1), pow(2, _lambda/2))
    q = random.randrange(pow(2, _lambda/2 - 1), pow(2, _lambda/2))
    while (q == p or is_prime(q) == False):
        q = random.randrange(pow(2, _lambda/2 - 1), pow(2, _lambda/2))

    return (p,q)




# TODO: Tao thong diep m
def mes_gen():
    m = random.randrange(0, pow(2, _lambda/2 - 1))
    return m




# TODO: Tim nghich dao cua so e
def mod_inverse(e, phi):
    temp_phi = phi 
    x = 0
    d = 1
  
    if (phi == 1): 
        return 0
  
    while (e > 1): 
        y = e // phi 
        temp = phi 
        phi = e % phi 
        e = temp
        temp = x 
        x = d - y * x 
        d = temp 
  
    if (d < 0): 
        d = d + temp_phi 
  
    return d



# TODO:  Khoi tao khoa private va public
def key_pair(p, q):
    
    n = p * q
    phi = (p-1) * (q-1)

    e = random.randrange(2, phi)
    gcd = GCD(e, phi)
    
    while (gcd != 1):
        e = random.randrange(2, phi)
        gcd = GCD(e, phi)

    d = mod_inverse(e, phi)

    # (n,e) la khoa cong khai
    # (n,d) la khoa bi mat
    return ((n, e), (n, d)) 




# TODO: Ma hoa
def encrypt(pkey, plaintext):
    n, key = pkey
    cipher = pow(plaintext, key, n)

    return cipher

# TODO: Giai ma
def decrypt(pkey, ciphertext):
    n, key = pkey
    plaintext = pow(ciphertext, key, n)

    return plaintext



# _main_
prime = prime_gen()
p = prime[0]
q = prime[1]


print("\n##### Generating key . . . #####")
start_time = time.time()
public, private = key_pair(p, q)
print("Generated key in %fs." % (time.time() - start_time))
print("> Public Key : ",public)
print("> Private Key :" ,private)



message = mes_gen()
print('\nMessage:',message)



print("\n##### Encrypting . . . #####")
start_time = time.time()
encrypted_text = encrypt(public, message)
print("Encrypted in %fs." % (time.time() - start_time))
print('> Encrypted Message:', encrypted_text)



print("\n##### Decrypting . . . #####")
start_time = time.time()
decrypted_text = decrypt(private, encrypted_text)
print("Decrypted in %fs." % (time.time() - start_time))
print('> Decrypted Message:', decrypted_text, '\n')

