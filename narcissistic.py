from functools import reduce

def narcissistic(value):
  str_value = str(value)
  list_value = map(lambda s: int(s) ** len(str_value), str_value)
  result = reduce(lambda x, y: x + y, list_value)

  return result == value

print(narcissistic(7) == True);
print(narcissistic(371) == True);
print(narcissistic(122) == False);
print(narcissistic(4887) == False);