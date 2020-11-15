import time
from RSA.data import *
from RSA.rsa import *
from RSA.rsa_oaep import *

if __name__ == '__main__':
    message = bytearray(input(), "ascii")

    for i in range(512, 1025, 128):
        x, y = interval(i)

        p = prime_generation(x, y)
        print("p: {0}".format(p))
        q = p
        while p == q:
            q = prime_generation(x, y)
        print("q: {0}".format(q))
        N = p * q
        print("N: {0}".format(N))
        f = (p - 1) * (q - 1)
        print("f: {0}".format(f))
        e = prime_generation(3, f - 1)
        while math.gcd(f, e) != 1:
            e = prime_generation(3, f - 1)
        print("e: {0}".format(e))
        d = pow(e, -1, f)
        if d == e:
            d += f
        print("d: {0}".format(d))
        print()

        start_time = time.time()
        cipher = rsa_encrypt(N, e, message, i)
        decr_m = rsa_decrypt(d, cipher, p, q)
        print("Result: " + decr_m.decode())
        end_time = time.time()
        print("RSA-{0}:  %f seconds".format(i) % (end_time - start_time))

        g = ((i // 128) // 2) * 128
        h = i - g

        start_time = time.time()
        cipher = rsa_oaep_encrypt(N, e, message, g, h)
        decr_m = rsa_oaep_decrypt(d, cipher, p, q, g, h)
        print("Result: " + decr_m.decode())
        end_time = time.time()
        print("RSA OAEP-{0}:  %f seconds".format(i) % (end_time - start_time))
        print()
