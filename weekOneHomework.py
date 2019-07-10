# create code w/following requirements 
# 1. Variable 'confused' should be present in 3 scopes
# 2. Use 'global' or 'nonlocal' keyword

import sys
import string
from random import sample

class Scramble:
    def __init__(self, keyword="confused", rows=8):
        self.keyword = keyword
        self.rows = [row+1 for row in range(rows)]
    
    def createScramble(self):
        aToZ = string.ascii_letters
        return scrambleList = [random.sample(aToZ,len(rows)) for row in rows]

    