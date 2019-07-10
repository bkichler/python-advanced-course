# create code w/following requirements 
# 1. Variable 'confused' should be present in 3 scopes
# 2. Use 'global' or 'nonlocal' keyword

import sys
import string
import random

confusion = "confused"
_global = "nonlocal"
_local = ""

class Scramble:

    def __init__(self, keyword, rows=8):
        global confusion
        self.keyword = "what?"
        self.rows = [row+1 for row in range(rows)]
    
    def createScrambleList(self):
        aToZ = string.ascii_letters + _global
        scrambleList = [random.sample(aToZ,len(self.rows)) for row in self.rows]
        return scrambleList

    def findGlobal(self):
        global _global
        global _local
        scrambleList = self.createScrambleList()
        for idx, array in enumerate(scrambleList):
            print(array)
            i = 0
            while i < len(array):
                if array[i].upper() == _global[i].upper():
                    _local += array[i]
                    break
                i += 1
    

new_scramble_obj = Scramble(confusion)
new_scramble_obj.findGlobal()

print(_local)

    