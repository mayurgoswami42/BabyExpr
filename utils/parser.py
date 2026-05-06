from .lexer import Lexer as lx

class Number:
    def __init__(self, value):
        self.value = value

class BinaryOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Parser:
    def __init__(self):
        self.text = ""
        self.data = list()
    
    def op_split(self, li: list):
        highest = -1
        index = 0
        p_rank = 0

        if (li[0][0] == '(' and li[0][2] == len(li) - 1):
            li.pop(0)
            li.pop()

        i = 0
        while i < len(li):
            if li[i][0] == '(':
                p_rank += 1
            elif li[i][0] == ')': p_rank -= 1

            if p_rank > 0:
                i += 1
                continue

            if li[i][1] > highest:
                highest = li[i][1]
                index = i
            i += 1
        
        return li[0:index], li[index], li[index+1:len(li)]
    
    def construct_tree(self, text = None, li = None):
        if (li == None):
            self.text = text
            lexer = lx()
            lexer.tokenize(self.text)
            self.data = lexer.labeled_data
            li = self.data
        
        if len(li) == 0:
            print("PARSER::ERROR:: Need input!")
            return BinaryOp([], [], [])

        if len(li) == 1: return li[0]
        left, op, right = self.op_split(li)

        if (len(left) == 0):
            print(f"PARSER::ERROR:: Expected a number before {op[0]}")
            return BinaryOp([], [], [])

        if (len(right) == 0):
            print(f"PARSER::ERROR:: Expected a number after {op[0]}")
            return BinaryOp([], [], [])
        if (len(left) == 1 and len(right) == 1): return BinaryOp(op, left[0], right[0])
        else: return BinaryOp(op, self.construct_tree(li = left), self.construct_tree(li = right))