# python example.py 5

import sys
from functools import reduce
from itertools import count, islice
from operator import add


def main(N):
    return reduce(add, islice(filter(lambda x: x % 2 == 0, map(lambda x: x + 1, count())), N))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        N = 5
    else:
        N = int(sys.argv[1])

    answer = main(N)
    print(answer)
