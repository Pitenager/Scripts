#!/usr/bin/env python3
from modsqrt import modular_sqrt 
# Taken from :
# https://gist.githubusercontent.com/nakov/60d62bdf4067ea72b7832ce9f71ae079/raw/864c0eb6e58329db8444a7a6fc3df28c0fc8580f/modsqrt.py
from Crypto.Util.number import long_to_bytes

p = 16561429133925410152910558138426342813003607408793210510350820778117750488294158025334154782168295150504888994664227526968840978993964333891214657448288057
q = 30126269920030533619149872131139522468497774940789529153525410135192816439227647545595239038914424116121815731200170441720580775486313620726576435961039567
n = p * q

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def bfs(ct):
    # Define queue
    queue = []
    queue.append(ct)
    while len(queue) != 0:
        # Pop element from queue 
        v = queue.pop(0)
        # Check if it's the right one
        if b'GrabCON{' in long_to_bytes(v):
            print(long_to_bytes(v))
            exit(0)
        # Computes...
        mp = modular_sqrt(v, p)
        mq = modular_sqrt(v, q)
        g, yp, yq = egcd(p, q)
        r1 = (yp * p * mq + yq * q * mp) % n
        r2 = n - r1
        r3 = (yp * p * mq - yq * q * mp) % n 
        r4 = n - r3
        possible_pt = [r1, r2, r3, r4]
        # Enqueue
        for pt in possible_pt:
            if not pt in queue:
                queue.append(pt)

def main():
    c = 9019127052844164572606928250741960583163943438936945828390420331200602392329
    bfs(c)

if __name__ == '__main__':
    main()

