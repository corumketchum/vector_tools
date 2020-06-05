###Loading relevant libraries 
#import pandas as pd

###puddles for data science credit: steve fickas 
#flush the old directory
#!rm -r  'uo_puddles'

#my_github_name = 'corumketchum'  #replace with your account name
#clone_url = f'https://github.com/{my_github_name}/uo_puddles.git'
#!git clone $clone_url 
#import uo_puddles.uo_puddles as up

###spaCy key functions for tokenizing and analyzing language 

#import spacy
#!python -m spacy download en_core_web_md

###Bring in english language for use with spaCy (can replace with other language library)
#import en_core_web_md
#nlp = en_core_web_md.load()

####methods start here 

####Subtracting  vectors 
def subtractv(x:list, y:list) -> list:
  assert isinstance(x, list), f"x must be a list but instead is {type(x)}"
  assert isinstance(y, list), f"y must be a list but instead is {type(y)}"
  assert len(x) == len(y), f"x and y must be the same length"

  #result = [(c1 - c2) for c1, c2 in zip(x, y)]  #one-line compact version - called a list comprehension

  result = []
  for i in range(len(x)):
    c1 = x[i]
    c2 = y[i]
    result.append(c1-c2)

  return result
  
###Adding Vectors 
def addv(x:list, y:list) -> list:
  assert isinstance(x, list), f"x must be a list but instead is {type(x)}"
  assert isinstance(y, list), f"y must be a list but instead is {type(y)}"
  assert len(x) == len(y), f"x and y must be the same length"

  #result = [c1 + c2 for c1, c2 in zip(x, y)]  #one-line compact version

  result = []
  for i in range(len(x)):
    c1 = x[i]
    c2 = y[i]
    result.append(c1+c2)

  return result
 
###Dividing Vectors
def dividev(x:list, c) -> list:
  assert isinstance(x, list), f"x must be a list but instead is {type(x)}"
  assert isinstance(c, int) or isinstance(c, float), f"c must be an int or a float but instead is {type(c)}"

  #result = [v/c for v in x]  #one-line compact version

  result = []
  for i in range(len(x)):
    v = x[i]
    result.append(v/c) #division produces a float

  return result

###mean of vectors
def meanv(matrix: list) -> list:
    assert isinstance(matrix, list), f"matrix must be a list but instead is {type(x)}"
    assert len(matrix) >= 1, f'matrix must have at least one row'

    #Python transpose: sumv = [sum(col) for col in zip(*matrix)]

    sumv = matrix[0]  #use first row as starting point in "reduction" style
    for row in matrix[1:]:   #make sure start at row index 1 and not 0
      sumv = addv(sumv, row)
    mean = dividev(sumv, len(matrix))
    return mean

###Find the vector of a word 
def get_vec(s:str) -> list:
    return nlp.vocab[s].vector.tolist()
 
###Converts whole sentences to vectors dependent on all above
def sent2vec(sentence: str) -> list:

  matrix = []

  doc = nlp(sentence.lower())

  for i in range(len(doc)):
    token = doc[i]
    if token.is_alpha and not token.is_stop:
      vec = get_vec(token.text)
      matrix.append(vec)

  result = [0.0]*300
  if len(matrix) != 0:
    result = meanv(matrix)
  return result
