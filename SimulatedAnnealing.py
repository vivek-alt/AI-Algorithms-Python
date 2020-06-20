# Optimize f(x)=x^3-60x^2+900x+100 using simulated annealing algorithm
import random
import math


def f(x):
    return x ** 3 - 60 * x * x + 900 * x + 100


def generate(State, Move):
    return State[:Move - 1] + ('1' if State[Move - 1] == '0' else '0') + State[Move:]


T = 500  # Start temp
S = '10011'  # start state
Tmin = 1
iters = 100
while True:
    i = 1
    while True:
        move = random.randint(1, 5)
        s = generate(S, move)
        E = f(int(S, 2)) - f(int(s, 2))
        if E <= 0:
            S = s
        elif random.random() <= math.exp(-E / T):
            S = s
        # print(S, f(int(S, 2)), s, f(int(s, 2)))
        if i >= iters:  # Inner termination condition
            break
        i += 1

    T = 0.9 * T  # Temp update

    if T < Tmin:  # Termination condition
        break
    print(S, f(int(S, 2)))
print('f(', S, ')=', f(int(S, 2)))
