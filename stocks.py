import sys

def best_gain(ss):
    high, low, nextlow = 0, sys.maxint, sys.maxint
    for s in ss:
        if s < nextlow:
            nextlow = s
        if s - nextlow > (high - low):
            low = nextlow
            high = s
    print [low, high]

best_gain([55,44,33,44,55,66,111,66,22,77,99,101,35])    

# returns [22, 101]
