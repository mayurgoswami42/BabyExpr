def evaluate(expression): 
  tokens = tokenize(expression) 
  if not tokens: 
    return None 
  result = tokens[0] 
  for token in tokens[1:]: 
    if token == '/': 
      result = result / float(tokens[tokens.index(token) + 1]) 
    else: 
      result = result + float(token) 
  return result 

# Test case: 20/2/2 
print(evaluate('20/2/2'))