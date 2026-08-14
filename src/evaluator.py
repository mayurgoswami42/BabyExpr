def evaluate(expression): 
  tokens = expression.split('/') 
  result = float(tokens[0]) 
  for token in tokens[1:]: 
    result /= float(token) 
  return result 
