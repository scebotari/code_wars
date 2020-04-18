def dirReduc(arr):
  to_reduce = (
    ("NORTH", "SOUTH"),
    ("SOUTH", "NORTH"),
    ("WEST", "EAST"),
    ("EAST", "WEST")
  )
  result = arr[:]

  i = 0
  while i < len(result) - 1:
    print(result, i)
    if (result[i], result[i + 1]) in to_reduce:
      result[i:(i + 2)] = []
      if i > 0: i -= 1
    else:
      i += 1

  return result

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a) == ['WEST'])
u = ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u) == ["NORTH", "WEST", "SOUTH", "EAST"])