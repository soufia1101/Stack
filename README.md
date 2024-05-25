# Stack Data Implementation and Applications

## Introduction
This assignment challenges you to understand and implement stack operations through a series of tasks that involve problem solving and algorithm development using the stack data structure. By completing these tasks, you'll gain practical experience in using stacks for various applications.

## Learning Outcomes
After completing this assignment, you should be able to:

Implement and understand the operations of a stack.
Apply stacks in various scenarios such as expression evaluation, data sorting, and problem solving.

### Task 1: Implementing the Stack Class
Develop a Stack class using a Python list to handle element storage. This class should support several methods:

* `push(item)`: Adds an item to the top of the stack.

* `pop()`: Removes the item at the top of the stack and returns it. Returns None if the stack is empty.

* `peek()`: Returns the top item of the stack without removing it. Returns None if the stack is empty.

* `isEmpty()`: Returns True if the stack is empty, otherwise False.

* `size()`: Returns the number of elements in the stack.
* `get_max()`: Retrieve the maximum element in the stack.

#### Example:
```
stack = Stack()
stack.push(100)
stack.push(10)
stack.push(20)
print(stack.get_max) # output: 100
print(stack.peek()) # Output: 20
print(stack.pop()) # Output: 20
print(stack.isEmpty()) # Output: False
```

### Task 2: String Reversal
Implement a function reverse_string(input_string) that uses your stack to reverse the characters in a string.

#### Example:
```
print(reverse_string("hello")) # Output: "olleh"
```
### Task 3: Postfix Expression Evaluation
Write a function evaluate_postfix(expression) that evaluates a postfix expression where each element is spaced apart.

#### Example:
```
print(evaluate_postfix("3 4 + 2 * 7 /")) # Output: 2
```

### Task 4: Balanced Symbols Check
Develop a function is_balanced(expression) to check if all types of brackets are balanced in the expression.

#### Example:
```
print(is_balanced("{[()]}")) # Output: True
print(is_balanged("({[)")) # Output: False
```
### Task 5: Prefix to Postfix Conversion
Convert a prefix expression to a postfix expression using a stack.

#### Example:
```
print(prefix_to_postfix("* + 3 4 2")) # Output: "3 4 + 2 *"
```
### Task 6: Sort Stack
Implement sort_stack() which sorts a stack so that the smallest items are on the top.

#### Example:
```
stack = Stack()
stack.push(3)
stack.push(1)
stack.push(4)
sorted_stack = sort_stack(stack)
print(sorted_stack.pop()) # Output: 1
print(sorted_stack.pop()) # Output: 3
```

### Task 7: Infix to Postfix Conversion
Convert an infix expression to a postfix expression using the stack. Ensure the function handles operator precedence correctly.

#### Example:
```
print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )")) # Output: "3 4 2 * 1 5 - / +"
```

### Task 8: Daily Temperatures
Given a list of daily temperatures, output how many days until a warmer temperature. If there is no future warmer day, output 0.

#### Example:
```
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])) # Output: [1, 1, 4, 2, 1, 1, 0, 0]
```
### Task 9: Longest Valid Parentheses
Use a stack to find the length of the longest valid (well-formed) parentheses substring. For a given string containing just the characters '(' and ')', find the length of the longest substring that is well-formed.

#### Example:
```
print(longest_valid_parentheses("(()"))  # Output: 2
print(longest_valid_parentheses(")()())"))  # Output: 4
```
Explanation: The longest valid parentheses substring in the first example is "()", which has a length of 2. In the second example, the longest substring is "()()", which has a length of 4.

### Submission Requirements
Submit a Python script named stack_exercises.py containing the Stack class and all function implementations. Ensure your script is well-commented.

### Evaluation Criteria

* Correctness and efficiency of the implemented stack operations.
* Accuracy in solving the assigned problems using the stack.
* Clarity and readability of the code.