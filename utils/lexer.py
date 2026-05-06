from .tokens import Token as tk, TOKENS

class Lexer:
    def __init__(self):
        self.text = ""
        self.labeled_data: list[list[str]] = list()
        self.pos = 0

    def next_token(self):
        if self.pos >= len(self.text):
            return ['', tk.EOF]
        
        while self.pos < len(self.text) and self.text[self.pos] == ' ':
            self.pos += 1
        
        if self.text[self.pos] in TOKENS:
            li = [self.text[self.pos], TOKENS[self.text[self.pos]]]
            self.pos += 1
            return li
        
        number = ""
        while self.pos < len(self.text) and (self.text[self.pos]).isdigit():
            number += self.text[self.pos]
            self.pos += 1

        if number != "":
            return [number, tk.NUMBER]
        
        alpha = ""
        while self.pos < len(self.text) and (self.text[self.pos]).isalpha():
            alpha += self.text[self.pos]
            self.pos += 1

        if alpha != "":
            return [alpha, tk.IDENTIFIER]
        
        return [self.text[self.pos], tk.UNDEFINED]
    
    def tokenize(self, text: str):
        p_indices = list()
        self.text = text.strip()
        next = self.next_token()
        while next[1] != tk.EOF:
            if next[0] == '(':
                p_indices.append(len(self.labeled_data))
            elif next[0] == ')':
                pos_lp = p_indices[len(p_indices) - 1]
                pos_rp = len(self.labeled_data)
                self.labeled_data[pos_lp].append(pos_rp - pos_lp)
                p_indices.pop()
            self.labeled_data.append(next)
            next = self.next_token()
        
        if len(p_indices) != 0:
            print("LEXER::ERROR:: Expected a \")\"")
            return