from utils.evaluator import Evaluator
from utils.status_manager import StatusManager, STATUS

s = StatusManager()

evaluator = Evaluator(s)

if __name__ == "__main__":
    inp = input(">> ")
    while inp != 'exit':
        inp = evaluator.evaluate(inp)
        if s.get_status() == STATUS.BAD:
            break
        print(evaluator.evaluate(inp))
        inp = input(">> ")