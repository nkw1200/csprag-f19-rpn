#!/usr/bin/env python3

import operator
#from colorama import Fore
#from colorama import Style

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '^': operator.pow,
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
            
       # print(stack)
    if len(stack) != 1:
        raise TypeError('Malformed input')
    return stack.pop()    

def printetc():
    print("ff")
    print("ff")
    print("aasdf")

def main():
    while True:
        #result = calculate(input(Fore.RED + "rpn calc> "))
        result = calculate(input("rpn calc>"))
        print(result)
    #printetc()
if __name__=='__main__':
    main()
    
