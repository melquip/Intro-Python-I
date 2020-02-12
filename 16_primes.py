import random
from math import sqrt
running = True
while running:
  num = int(input("Hey, I'll give you some gold for primes!\n"))
  if num > 1:
    sqrtNum = int(sqrt(num))
    print('sqrtNum:' + str(sqrtNum))
    # list of integers from 2 to num
    primes = []
    for i in range(2, num+1):
        primes.append(i)
    # loop through the square root of num
    for i in range(2, sqrtNum+1):
      print('hum... i:' + str(i))
      if i in primes:
        for j in range(i*2, num+1, i):
          print('hum... j:' + str(j))
          if j in primes:
            print('hum... removed j:' + str(j))
            primes.remove(j)

    # check if num is prime or not
    if num in primes:
      running = False
      print(f'Yes! {num} is a PRIME! Here you go, {int(random.random() * 1000) + 10 } gold, your reward!')
    else:
      print(f'NO! {num} is NOT a prime! Don\'t try to trick me, stranger!\n\n')
  else:
    print('Oops, try again! We need a positive number greater than 1!')