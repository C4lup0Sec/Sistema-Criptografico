import random
max_PrimLength = 100
'''
Cacular el modulo inverso de e y z
'''
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

'''
Calcular el mcd de dos numeros
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Checar si es un numero primo
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generateRandomPrim():
    while(1):
        ranPrime = random.randint(0,max_PrimLength)
        if is_prime(ranPrime):
            return ranPrime

def generate_keyPairs():
    p = generateRandomPrim()
    q = generateRandomPrim()
    
    n = p*q
    print("n ",n)
    '''z(n) = z(p)*z(q)'''
    z = (p-1) * (q-1) 
    print("z ",z)
    
    '''choose e coprime to n and 1 > e > z'''    
    e = random.randint(1, z)
    g = gcd(e,z)
    while g != 1:
        e = random.randint(1, z)
        g = gcd(e, z)
        
    print("e=",e," ","z=",z)
    '''d[1] = modular inverse of e and z'''
    d = egcd(e, z)[1]
    
    '''make sure d is positive'''
    d = d % z
    if(d < 0):
        d += z
        
    return ((e,n),(d,n))
        
def decrypt(ctext,private_key):
    try:
        key,n = private_key
        text = [chr(pow(char,key,n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)

def encrypt(text,public_key):
    key,n = public_key
    ctext = [pow(ord(char),key,n) for char in text]
    return ctext

if __name__ == '__main__':
    public_key,private_key = generate_keyPairs() 
    print("Public: ",public_key)
    print("Private: ",private_key)
    
    ctext = encrypt("155",public_key)
    print("encrypted  =",ctext)
    plaintext = decrypt(ctext, private_key)
    print("decrypted =",plaintext)
  
