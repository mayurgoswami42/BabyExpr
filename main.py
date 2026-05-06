from utils.evaluator import Evaluator

evalu = Evaluator()

inp = input(">> ")
while inp != 'exit':
    print(evalu.evaluate(inp))
    inp = input(">> ")