from convert import str_to_float

def gather_numbers() -> list[float]:
    result = []
    take_input = input("Enter a number or if you are done type 'done'")
    while take_input!= "done":
        num = str_to_float(take_input)
        if num:
            result.append(num)
        take_input = input("Enter a number or if you are done type 'done'")
    return result


if __name__ == '__main__':
    numbers = gather_numbers()
    print("The sum is:", sum(numbers))
#This function takes input from the user in the form of a list of numbers. Then it will pass the input to the str_to_float function in convert.py and attempt to convert the inputted text into floats. The float values are then appended to a list and summed when the function is called.
#Testing can be performed in the console.

#10, 1 --> The sum is 11.0
#10000 --> The sum is 10000.0
#"word" --> The sum is 0