import sys
from convert import str_to_float


def sum_commandline()-> float:
    sum = 0.0
    for i in range(1, len(sys.argv)):
        num = str_to_float(sys.argv[i])
        if num is not None:
            sum += num
    return sum


if __name__ == '__main__':
    result = sum_commandline()
    print("The sum is", result)

#The purpose of this function is to do the same thing as keyboard, taking in a list of numbers or strings are attempting to convert them to a float if possible, then finally summing all the floats.
#However this function take inputs directly from the command line unlike keyboard.py.
#Testing can be performed by inputting the specific parameters by editing file configuration.

#command_line.py 9, 10, 11 --> The sum is 30.0