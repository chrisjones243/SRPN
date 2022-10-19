import random # for random number generation
import re 

stack = [] # the stack

# @params - the operator(+, -, ...) needed to solve the expression, x and y are the operands
# this func. will use a dictionary to calculate the expression
# @return - returns the result of the expression
def expression(operator, x, y):
  switcher = {
    '+': y + x,
    '-': y - x,
    '*': y * x,
    '/': y / x,
    '^': y ** x,
    '%': y % x
  }
  return int(switcher.get(operator))


# @params - the operator(+, -, ...) needed to solve the expression
# this func. will pop the top two elements of the stack and call the expression func. to solve the expression
def handleOperator(operator):
  global stack
  try: # try to pop the top two elements of the stack
    x = stack.pop()
    y = stack.pop()
  except IndexError:
    print("Stack Underflow.")
    return 0
  if operator == '/' and x == 0:
    print("Divide by 0")
    return 0
  else:
    result = expression(operator, x, y)
    if result < -2147483648:
      stack.append(-2147483648) # if the result is less than the min value of an int, then append the min value
      return 0
    elif result > 2147483647:
      stack.append(2147483647) # if the result is greater than the max value of an int, then append the max value
      return 0
    else:
      stack.append(result) # if the result is in the range of an int, then append the result
      return 0

  
def handleUnknowValueError(exception):
  try:
    combination = re.split('\d', exception)
    for x in combination:
      print(x)
      process_command(x)
  except TypeError:
    print("Unrecognised operator or operand '" + exception + "'.")

# @params - the string the user has typed
# this func. will check the command and call the appropriate func.
def handleValueError(exception):
  global stack

  if exception == 'r':
    stack.append(random.randint(-2147483648, 2147483647))  # append the random integer to the stack
  elif exception == 'd':
    for x in stack:
      print(x) # prints the stack
  elif exception == '=':
    try:
      print(stack[-1]) # prints the top element of the stack
    except IndexError:
      print("Stack empty.")
  elif exception == ['+', '-', '*', '/', '^', '%']: # if the element is an operator
    handleOperator(exception) # call the handleOperator func.
  else:
    handleUnknowValueError(exception) # if the element is not an operator, call the handleUnknowValueError func.
    
    

# @params - the string the user has typed
# 
def process_command(command):
  global stack
  commentFlag = False

  command = command.split() # splits the string into an array
  for x in command: # for each element in the array
      if x == '#': 
        commentFlag = not commentFlag # if the element is a comment, then the commentFlag will be flipped
      elif commentFlag: 
        continue  # if the commentFlag is true, then the loop will continue
      else:
        try:
          stack.append(int(x)) # if the element is an integer, append it to the stack
        except ValueError: 
          handleValueError(x) # if the element is not an integer, call the handleValueError func. to check if it is a command
        except OverflowError:
          print("Stack Overflow") # if the element is too large, then the stack is overflowed


#This is the entry point for the program.
#It is suggested that you do not edit the below,
#to ensure your code runs with the marking script
if __name__ == "__main__": 
  while True:
    try:
      cmd = input()
      pc = process_command(cmd)
    except EOFError: 
      exit()
