from utils.evaluator import Evaluator
from utils.status_manager import StatusManager, STATUS

s = StatusManager()

evalu = Evaluator(s)

inp = input(">> ")
while inp != 'exit':
    inp = evalu.evaluate(inp)
    if s.get_status() == STATUS.BAD:
        break
    print(evalu.evaluate(inp))
    inp = input(">> ")