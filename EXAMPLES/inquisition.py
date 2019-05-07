#!/usr/bin/python3

"""
    NOONE expects the spanish inquistion
"""

import random

device = "Comfy chair"

torture_words = ('Sit','Stay','Confess','Hm! She is made of harder stuff')

def _get_random_torture_word():
    """ get a phrase for the Grand Inquisitor to speak """
    return random.choice(torture_words)

def torture():
    """ strap someone into the comfy chair """
    word = _get_random_torture_word()
    print(word )

def intimidate():
    """ Enumerate our weapons """
    print('Amongst our weaponry are such diverse elements as fear, surprise, ruthless efficiency, an almost fanatical devotion to the Pope, and nice red uniforms!')

# testing code
if __name__ == '__main__':
    intimidate()
    print()
    print("Bring out the",device)
    torture()
