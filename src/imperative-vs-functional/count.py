array = [1, 2, 3]
list(map(print, array)) # 1 2 3

print(list(filter(lambda x: x % 2 == 0, array))) # [2]

from functools import reduce
from operator import add

print(reduce(add, array, 0)) # 6

