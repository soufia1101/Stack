# stack_exercises.py

class Stack:
    def __init__(self):
        self.items = []
        self.max_stack = []

    def push(self, item):
        self.items.append(item)
        if not self.max_stack or item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        item = self.items.pop()
        if item == self.max_stack[-1]:
            self.max_stack.pop()
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.is_empty():
            return None
        return self.max_stack[-1]


# Task 2: String Reversal
def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string


# Task 3: Postfix Expression Evaluation
def evaluate_postfix(expression):
    stack = Stack()
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
    return stack.pop()


# Task 4: Balanced Symbols Check
def is_balanced(expression):
    stack = Stack()
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in matching_pairs.values():
            stack.push(char)
        elif char in matching_pairs.keys():
            if stack.is_empty() or stack.pop() != matching_pairs[char]:
                return False
    return stack.is_empty()


# Task 5: Prefix to Postfix Conversion
def prefix_to_postfix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])
    expression = expression.split()[::-1]
    for token in expression:
        if token in operators:
            a = stack.pop()
            b = stack.pop()
            stack.push(f"{a} {b} {token}")
        else:
            stack.push(token)
    return stack.pop()


# Task 6: Sort Stack
def sort_stack(stack):
    temp_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    return temp_stack


# Task 7: Infix to Postfix Conversion
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = Stack()
    output = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (not stack.is_empty() and stack.peek() != '(' and
                   precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
    while not stack.is_empty():
        output.append(stack.pop())
    return ' '.join(output)


# Task 8: Daily Temperatures
def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = Stack()
    for i, temp in enumerate(temperatures):
        while not stack.is_empty() and temperatures[stack.peek()] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.push(i)
    return result


# Task 9: Longest Valid Parentheses
def longest_valid_parentheses(s):
    stack = Stack()
    stack.push(-1)
    max_length = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.push(i)
        else:
            stack.pop()
            if stack.is_empty():
                stack.push(i)
            else:
                max_length = max(max_length, i - stack.peek())
    return max_length


# Example usage
if __name__ == "__main__":
    # Task 1: Stack Class
    stack = Stack()
    stack.push(100)
    stack.push(10)
    stack.push(20)
    print(stack.get_max())  # Output: 100
    print(stack.peek())  # Output: 20
    print(stack.pop())  # Output: 20
    print(stack.is_empty())  # Output: False

    # Task 2: String Reversal
    print(reverse_string("hello"))  # Output: "olleh"

    # Task 3: Postfix Expression Evaluation
    print(evaluate_postfix("3 4 + 2 * 7 /"))  # Output: 2

    # Task 4: Balanced Symbols Check
    print(is_balanced("{[()]}"))  # Output: True
    print(is_balanced("({[)"))  # Output: False

    # Task 5: Prefix to Postfix Conversion
    print(prefix_to_postfix("* + 3 4 2"))  # Output: "3 4 + 2 *"

    # Task 6: Sort Stack
    stack = Stack()
    stack.push(3)
    stack.push(1)
    stack.push(4)
    sorted_stack = sort_stack(stack)
    print(sorted_stack.pop())  # Output: 1
    print(sorted_stack.pop())  # Output: 3

    # Task 7: Infix to Postfix Conversion
    print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )"))  # Output: "3 4 2 * 1 5 - / +"

    # Task 8: Daily Temperatures
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]

    # Task 9: Longest Valid Parentheses
    print(longest_valid_parentheses("(()"))  # Output: 2
    print(longest_valid_parentheses(")()())"))  # Output: 4
