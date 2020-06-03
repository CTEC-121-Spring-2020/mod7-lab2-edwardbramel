"""
CTEC 121
Edward lamanna
modeul 7 lab 2
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

'''
def main():
    
     x = 1
     y = 2
     z = 3
     print("x: {0}, y: {1}, z: {2}".format(x, y, z))

     print("pi:", pi, "e:", e)
     print("pi: {0:0.2f}, e: {1:0.2f}".format(pi, e))
     print("pi: {0:10.2f}, e: {1:10.2f}".format(pi, e))
 '''
from math import *
    # file processing
print()
infile = open("sample.txt", 'r')
print(infile)
'''
    # get everything
    wholeFileText = infile.read()
    print(wholeFileText)
    print()
    print("----")
    print()
    infile.seek(5)
    wholeFileText = infile.read()
    print("*", wholeFileText, "*", sep="")
    '''
'''
    # demo readline()
    wholeFileTextaslist = infile.readlines()
    print(wholeFileTextaslist)
    for line in wholeFileTextaslist:
        print(line.rstrip())
    '''
# demo file a line at a time
'''
    for line in infile:
        print(line, end="")

    line = infile.readline()
    while line != "":  # eqvil to while not end of file
        print(line.rstrip())
        # get next line
        line = infile.readline()
    '''


# dictionaries
'''
    dict1 = {}
    print(dict1)

    dict2 = {}
    dict2[1] = "one"
    dict2[2] = "two"
    dict2[3] = "three"
    print(dict2)

    dict1 = {1: 'one', 2: 'two', 3: 'three'}
    print(dict1)

    print(dict1[2])
    print()
    print(dict1.keys())
    print(dict1.values())
    print(dict1.items())
   # print(dict1.items([2][1]))
'''


def main():
    '''
    num = 1234
    print("num:", num)
    processprimitivearg(num)
    print("num:", num)

    def processprimitivearg(x):
    print("input value: ", x)
    x = 99
    print("final value: ", x)


    print()
    '''

    num = [1234]
    print("num:", num)
    processlistarg(num)
    print("num:", num)
    print()


def processlistarg(l):
    print("input list:", l)
    l[0] = 99
    print("final list:", l)


main()
