 #!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    
    c1 = Counter(a)
    c2 = Counter(b)
    cmn = c1&c2
    key = 0
    for i in cmn:
        key = key + cmn[i]
        
    return (len(a)-2*key+ len(b))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
