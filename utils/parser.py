from .lexer import Lexer as lx

class Number:
    def __init__(self, value):
        self.value = value

class BinaryOp: # tree struct
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Parser:
    def __init__(self, manager):
        self.manager = manager
        self.text = ""
        self.data = list()

    # splitting the expression by operator, 3 + 2 * 4 => left: 3 + 2 | operator: * | right: 4
    def op_split(self, li: list):
        highest = -1
        index = 0
        parenthesis_depth = 0

        i = 0
        while i < len(li):
            if li[i][0] == '(':
                parenthesis_depth += 1
            elif li[i][0] == ')': parenthesis_depth -= 1

            if parenthesis_depth > 0:
                i += 1
                continue

            if li[i][1] > highest:
                highest = li[i][1]
                index = i
            i += 1

        if li[index][1] < 4 or li[index][1] > 8:
            self.manager.throwE(f"PARSER::ERROR:: Unknown operator \"{li[index][0]}\"")

        return li[0:index], li[index], li[index+1:len(li)]

    def construct_tree(self, text = None, li = None):
        if (li == None):
            self.text = text
            lexer = lx(self.manager)
            lexer.tokenize(self.text)
            self.data = lexer.labeled_data
            li = self.data # li is list of characters with precedence,  [[c1, precedence], [c2, precedence], ...]
        
        if len(li) == 0:
            self.manager.throwE("PARSER::ERROR:: Need input!") # prints the error and updates the status to bad so the execution could be stopped
            return BinaryOp([], [], [])

        # popping out useless parenthesis, eg: (2 + 3) => 2 + 3
        if (li[0][0] == '(' and li[0][2] == len(li) - 1):
            li.pop(0)
            li.pop()

        if len(li) == 1: return li[0]
        left, op, right = self.op_split(li)

        if (len(left) == 0):
            self.manager.throwE(f"PARSER::ERROR:: Expected a number before {op[0]}") # prints error, status => bad
            return BinaryOp([], [], [])

        if (len(right) == 0):
            self.manager.throwE(f"PARSER::ERROR:: Expected a number after {op[0]}") # prints error, status => bad
            return BinaryOp([], [], [])
        
        if (len(left) == 1 and len(right) == 1): return BinaryOp(op, left[0], right[0]) # base case of recursion
        else: return BinaryOp(op, self.construct_tree(li = left), self.construct_tree(li = right)) # recursive case