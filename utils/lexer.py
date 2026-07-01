from .tokens import Token as tk, TOKENS

class Lexer:
    def __init__(self, manager):
        self.manager = manager
        self.text = ""
        self.labeled_data: list[list[str]] = list()
        self.pos = 0
    
    def get_token(self, pos, text):
        if pos >= len(text):
            return pos, ['', tk.EOF]
        
        while pos < len(text) and text[pos] == ' ':
            pos+=1
        
        if text[pos] in TOKENS:
            li = [text[pos], TOKENS[text[pos]]]
            pos += 1
            return pos, li
        
        number = ""
        is_int = True
        while pos < len(text) and text[pos] in "0123456789.e":
            if text[pos] == 'e':
                if pos+1 < len(text) and text[pos+1] in "+-":
                    number += text[pos]
                    pos += 1

            if text[pos] == '.':
                if number == "": number += "0"
                is_int = False
            number += text[pos]
            pos += 1

        if number != '':
            if is_int:
                return pos, [int(number), tk.NUMBER]
            else: return pos, [float(number), tk.NUMBER]
        
        var = ""
        while pos < len(text) and text[pos].isalpha():
            var += text[pos]
            pos += 1
        
        if var != '':
            return pos, [var, tk.IDENTIFIER]
        
        token = [text[pos], tk.UNDEFINED]
        pos += 1
        return pos, token

    def tokenize(self, text: str):
        p_indices = list()
        text = str(text)
        self.text = text.strip()
        pos, next = self.get_token(0, text)
        while next[1] != tk.EOF:
            if next[0] == '(':
                p_indices.append(len(self.labeled_data))
            elif next[0] == ')':
                pos_lp = p_indices[len(p_indices) - 1]
                pos_rp = len(self.labeled_data)
                self.labeled_data[pos_lp].append(pos_rp - pos_lp)
                p_indices.pop()
            self.labeled_data.append(next)
            pos, next = self.get_token(pos, text)
        
        if len(p_indices) != 0:
            self.manager.throwE("LEXER::ERROR:: Expected a \")\"")
            return