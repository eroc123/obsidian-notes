import random, numpy as np, math
from sympy import isprime
def list_factors(n):
    factors = set()
    for i in range(1, int(np.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)



print(list_factors(12))


def game(number):
    choices = []
    factors = list_factors(number)
    gameEnd = False
    #emma does the first round and selects an element
    #1 is emma, 2 is nelly
    chosenNumber = random.choice(factors)
    factors.remove(chosenNumber)
    playerTurn = 'Nelly'
    while not gameEnd:
        choices = []
        if len(factors) == 0:
            gameEnd = True
            break
        for element in factors:
            if math.gcd(chosenNumber, element) == 1:
                choices.append(element)
        if len(choices) == 0:
            gameEnd = True
            break
        chosenNumber = random.choice(choices)
        factors.remove(chosenNumber)
        if playerTurn == 'Nelly':
            playerTurn='Emma'
        else:
             playerTurn = 'Nelly'
    return playerTurn

def checkPrimes(factors):
    primeCount = 0
    for i in factors:
        if isprime(i):
            primeCount+=1
    return primeCount

count = 0
for i in range(2, 100):
    factors = list_factors(i)
    if len(factors) > 6:
        count += 1
        print(i, ": ", factors)
print(count)
factors100 = []
for i in range(100):
    factors100.append(i)
print(checkPrimes(factors100))

factors = print(list_factors(2002), ": factors of 2002", checkPrimes(list_factors(2002)))