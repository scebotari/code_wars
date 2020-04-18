def order(sentence):
  sentence = sentence.split()
  sentence = list(map(get_index, sentence))
  sentence.sort()
  sentence = list(map(lambda word: word[-1], sentence))

  return ' '.join(sentence)

def get_index(word):
  for w in word:
    index = ord(w) - ord('0')
    if index >= 1 and index <= 9:
      return (index - 1, word)

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))


print(order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople")
print(order("") == "")