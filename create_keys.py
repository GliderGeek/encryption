from sympy import isprime
import json


def eulers_totient(p, q):
    return (p - 1) * (q - 1)


def n(_p, _q):
    return _p * _q


def d(_e, _phi):
    _d = 1
    while int(divmod(_e * _d, _phi)[1]) != 1:
        _d = _d + 1
    return _d


# ask user for first prime number
while True:
    print("Please insert the first prime number")
    print("p = ", end='')
    p = input()
    p = int(p)
    if isprime(p):
        break
    else:
        print("{} is not a prime number".format(p))

# ask user for second prime number
while True:
    print("Please insert a second, unequal, prime number")
    print("q = ", end='')
    q = input()
    q = int(q)
    if isprime(q):
        if q == p:
            print("q may not be equal to p")
        else:
            print('q = {}'.format(q))
            break
    else:
        print("{} is not a prime number".format(q))

# determine n, the modulus for both public and private keys. The bits of n is the key length
n = n(p, q)
# 3) phi is Eulers totient function which is the amount of numbers less than n that are coprime with p and q.
phi = eulers_totient(p, q)

while True:
    print("Choose 1 < e < {} such that {} and e are coprime. Choosing a prime number is an easy choice".format(phi, phi))
    print("e = ", end='')
    e = input()
    e = int(e)
    if phi % e == 0:
        print("phi may not be a multiplication of e")
    else:
        break

# determine d
d = d(e, phi)

# generate keys and save to keys.json
keys_dict = {
    'public': (e, n),
    'private': (d, n)
}
with open('keys.json', 'w') as f:
    json.dump(keys_dict, f)
