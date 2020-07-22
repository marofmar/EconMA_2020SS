# https://inventwithpython.com/dictionary.txt

import sys 
import os


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def load(file):
    """
    Open a text file and return a list of lowercase strings.
    """
    try:
        with open(os.path.join(__location__,file) as in_file:
            #s = in_file.readlines() 
            s = in_file.read().strip().split('\n')
            s = [x.lower() for x in s]
            return s 
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file = sys.stderr)
        sys.exit(1)

#print(load("/Users/yujinchung/Documents/EconMA_2020SS/lookingForPlindromes/dictionary.txt"))
          