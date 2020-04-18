def high_and_low(numbers):
  numbers = numbers.split()
  numbers = list(map(lambda x: int(x), numbers))

  return ' '.join([str(max(numbers)), str(min(numbers))])

print(high_and_low('1 2 9 10 -2 -5 22') == '22 -5')
print(high_and_low('1 2 9 10 -20 -5 22') == '22 -20')
print(high_and_low('100 2 9 10 -2 -5 22') == '100 -5')
