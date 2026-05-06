class Token:
    NUMBER = 0
    IDENTIFIER = 1
    LPAREN = 2
    RPAREN = 3
    MUL = 4
    DIV = 5
    PLUS = 6
    MINUS = 7
    EQUAL = 8
    UNDEFINED = 9
    EOF = 10

TOKENS = {
    '+': Token.PLUS,
    '-': Token.MINUS,
    '*': Token.MUL,
    '/': Token.DIV,
    '=': Token.EQUAL,
    '(': Token.LPAREN,
    ')': Token.RPAREN
}