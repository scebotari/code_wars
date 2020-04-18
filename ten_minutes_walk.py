def isValidWalk(walk):
  coordinates = [0, 0]
  moves = 0
  for w in walk:
    moves += 1
    move(w, coordinates)

  return moves == 10 and coordinates == [0, 0]

def move(direction, coordinates):
  if direction == 'n':
    coordinates[1] += 1
  elif direction == 's':
    coordinates[1] -= 1
  elif direction == 'e':
    coordinates[0] += 1
  elif direction[0] == 'w':
    coordinates[0] -= 1


print(isValidWalk(['n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 's']))
print(isValidWalk(['n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'e']))

print('test')
