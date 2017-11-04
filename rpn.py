#!/usr/bin/env python3

import operator
import readline
#from termcolor import colored
import logging, sys
import getopt
from colorama import init
init()
from colorama import Fore, Back, Style

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            stack.append(int(token))
            if ( int (token) < 0):
                print(Fore.RED + token + ' ',end='')
                print(Style.RESET_ALL,end='')
            else :
                print(token + ' ', end='')
        except ValueError:
            print(Fore.GREEN + token + '', end= '')
            print(Style.RESET_ALL)
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            result = function(arg1,arg2)
            stack.append(result)
    logging.debug(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main(argv):
    try: 
        opts, args = getopt.getopt(argv, "d","debug")
    except getopt.GetoptError:
        print ('Undefined argument')
    if ( opts and opts[0][0] in ('-d','--debug') ):
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    else:
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    while True:
        inputOption = input("rpn calc> ")
        if ( inputOption == "exit"):
            sys.exit()
        else:
            result = calculate(inputOption)
            print("Result: ", result)

if __name__ == '__main__':
    main(sys.argv[1:])
