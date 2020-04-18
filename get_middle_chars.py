def get_middle(s):
  start = len(s) // 2 - 1 + len(s) % 2
  end = start + 2 - len(s) % 2

  return s[start:end]

print(get_middle('test') == 'es')
print(get_middle('tests') == 's')
print(get_middle('Elena') == 'e')
