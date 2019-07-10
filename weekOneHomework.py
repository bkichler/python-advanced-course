# create code w/following requirements 
# 1. Variable 'confused' should be present in 3 scopes
# 2. Use 'global' or 'nonlocal' keyword

import sys
import string
import random

class Scramble:
    def __init__(self, keyword="confused", rows=8):
        self.keyword = keyword
        self.rows = [row+1 for row in range(rows)]
    
    def createScramble(self):
        aToZ = string.ascii_letters
        scrambleList = [random.sample(aToZ,len(self.rows)) for row in self.rows]
        return scrambleList

new_scramble_obj = Scramble()
scramble_list = new_scramble_obj.createScramble()

print(scramble_list)


    