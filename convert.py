from typing import Optional
def str_to_float(word: str)-> Optional[float]:
    try:
        return float(word)

    except ValueError:
        return None

#The purpose of this function is to take whatever string is passed to the function and if it is an int or float value it will convert it to float.
#If the string cannot be converted to a float (it is a word/alphabet/other character) then it will throw a ValueError and not return anything.
#Refer to convert_py.tests for testing.