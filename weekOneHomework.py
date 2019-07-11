# create code w/following requirements 
# 1. Variable 'confused' should be present in 3 scopes
# 2. Use 'global' or 'nonlocal' keyword

import sys
import string
import random
from colorama import init
init()
from colorama import Fore, Back, Style

confusion = "confused"
_global = "nonlocal"
_local = ""

class Scramble:
    """Instantiate confusion"""
    def __init__(self, rows=12):
        self.rows = [row+1 for row in range(rows)]
    
    def createScrambleList(self):
        """Create a nested list of scrambled ascii characters"""
        aToZ = string.ascii_letters + _global
        scrambleList = [random.sample(aToZ,len(self.rows)) for row in self.rows]
        return scrambleList

    def findGlobal(self):
        """Create a scrambled nested list and iterate over it.
        Add characters to the global _local string variable
        as they are found.
        """
        global _global
        scrambleList = self.createScrambleList()
        confusion = list(_global)
        letterIndex = 0
        currentLetter = confusion[letterIndex]
        def unnecessaryInnerFunction(letterList):
            global _local
            nonlocal confusion
            nonlocal currentLetter
            nonlocal letterIndex
            for array in scrambleList:
                i = 0
                while letterIndex < len(confusion) and i < len(scrambleList):
                    if _global.upper() == _local.upper():
                        break
                    elif array[i].upper() == currentLetter.upper():
                        if letterIndex == len(confusion)-1:
                            _local += array[i]
                            currentLetter = confusion[letterIndex]
                            print(array[0:i], Fore.GREEN + Style.BRIGHT + Back.CYAN + str([array[i]]) + Style.RESET_ALL, array[i+1:])
                            break
                        _local += array[i]
                        letterIndex += 1
                        currentLetter = confusion[letterIndex]
                        print(array[0:i], Fore.GREEN + Style.BRIGHT + Back.CYAN + str([array[i]]) + Style.RESET_ALL, array[i+1:])
                        break
                    else:
                        currentLetter = confusion[letterIndex]
                    i += 1
        unnecessaryInnerFunction(scrambleList)

    def determineConfusion(self):
        """Update the confusion string variable based on
        whether it finds a match between _global and _local
        """
        global confusion
        self.findGlobal()
        if _global.upper() == _local.upper():
            confusion = "slightly less confused"
        else:
            confusion = "still really confused"


new_scramble_obj = Scramble()
new_scramble_obj.determineConfusion()

print("Global equals "+_global+" and local equals "+_local+", so I'm "+confusion)

    