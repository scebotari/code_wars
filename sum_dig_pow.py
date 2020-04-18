def sum_dig_pow(a, b):
  result = []

  for number in range(a, b + 1):
    split = number_split(number)
    if number == sum(map(lambda x: x[1] ** (x[0] + 1), enumerate(split))):
      result.append(number)

  return result

def number_split(number):
  res = []
  divider = 10

  while number:
    res.append(number % 10)
    number //= divider

  return reversed(res)

print(sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
print(sum_dig_pow(10, 89) == [89])
print(sum_dig_pow(10, 100) == [89])
print(sum_dig_pow(90, 100) == [])
print(sum_dig_pow(89, 135) == [89, 135])
