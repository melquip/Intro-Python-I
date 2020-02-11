# https://repl.it/@melquip/Code-Challenge-Fibonacci

def fibonacciMaxNum(number):
  lastNum = 0
  nextNum = 1
  sequence = [0, 1]
  while nextNum + lastNum <= number:
    nextNum += lastNum
    lastNum = nextNum - lastNum
    sequence.append(nextNum)
  return sequence

print(fibonacciMaxNum(13))

def fibonacciMaxItems(number):
  previous_first = 0
  previous_second = 1
  next_num = 1
  sequence = [0]
  for i in range(1, number):
    next_num = previous_first + previous_second
    previous_first = previous_second
    previous_second = next_num
    if next_num == 1:
      sequence.append(next_num)
      number -= 1
    sequence.append(next_num)
  return sequence

print(fibonacciMaxItems(13))

# https://repl.it/@melquip/Code-Challenge-Harshad-numbers

import sys

def isHarshadNum(n):
  return n % (sum([int(char) for char in str(n)])) == 0

def harshad(number):
  cluster = []
  result = [0, 0]
  if isHarshadNum(number):
    cluster.append(number)
    for i in range(number + 1, int(sys.float_info.max), 1):
      # print('+1:', i)
      if not isHarshadNum(i):
        # print('break')
        break
      cluster.append(i)
    for i in range(number - 1, int(sys.float_info.min), -1):
      # print('-1:', i)
      if not isHarshadNum(i):
        # print('break')
        break
      cluster.insert(0, i)
    result = [len(cluster), cluster.index(number) + 1]
  return result

print(harshad(5))          # [10,5]
# print(harshad(133))      # [2,2]
# print(harshad(82))       # [0,0]
# print(harshad(72))       # [1,1]
# print(harshad(12751223)) # [6,4]
# print(harshad(5831))     # [3,1]
# print(harshad(10309))    # [4,3]
# print(harshad(7384))     # [0,0]
# print(harshad(2584))     # [1,1]
# print(harshad(1018))     # [0,0]

# https://repl.it/@melquip/Code-Challenge-removeDuplicates

def removeDuplicates(lst):
  return set(lst)

print(removeDuplicates([1,1,2,3,4,5,5])) # 1,2,3,4,5