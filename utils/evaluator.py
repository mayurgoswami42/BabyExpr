from .tokens import Token
from .parser import Parser, BinaryOp
from .status_manager import StatusManager

class Evaluator:
    def __init__(self, manager = None):
        self.manager = manager
        if self.manager is None: self.manager = StatusManager()
        self.parser = Parser(self.manager)
        self.store = {"inf" : "infinite", "nan" : "undefined"}
        
    def evaluate(self, text = None, tree = None):
        if tree is None:
            tree = self.parser.construct_tree(text)
        if not isinstance(tree, BinaryOp):
            if tree[1] == Token.NUMBER:
                return float(tree[0])
            elif tree[1] == Token.IDENTIFIER:
                if tree[0] in self.store.keys():
                    try:
                        return float(self.store[tree[0]])
                    except Exception as e:
                        self.manager.throwE(f"EVALUATOR::ERROR:: Exception \"{e}\"")
                else:
                    self.manager.throwE(f"EVALUATOR::ERROR:: Undefined variable \"{tree[0]}\"")
            else:
                self.manager.throwE(f"EVALUATOR::ERROR:: Bad Expression")
                return 0

        left_side = self.evaluate(tree = tree.left)
        right_side = self.evaluate(tree = tree.right)
        
        if (not isinstance(tree.left, BinaryOp) and len(tree.left) == 0) or (not isinstance(tree.right, BinaryOp) and len(tree.right) == 0):
            return 0
        if tree.op[1] == Token.PLUS:
            return left_side + right_side
        elif tree.op[1] == Token.MINUS:
            return left_side - right_side
        elif tree.op[1] == Token.MUL:
            return left_side * right_side
        elif tree.op[1] == Token.DIV:
            if right_side == 0:
                self.manager.throwE("EVALUATOR::ERROR:: Can't divide by 0!")
                return 0
            else:
                return left_side / right_side
        elif tree.op[1] == Token.EQUAL:
            if not isinstance(tree.left, BinaryOp) and tree.left[1] == Token.IDENTIFIER:
                self.store[tree.left[0]] = right_side
                return self.store[tree.left[0]]
            else:
                self.manager.throwE("EVALUATOR::ERROR:: Bad expression lvalue expexted before = ")
                return 0