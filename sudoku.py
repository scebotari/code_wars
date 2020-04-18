from functools import reduce

def validSolution(board):
  for i in range(0, 9):
    if len(get_row(board, i)) != 9:
      return False
    if len(get_col(board, i)) != 9:
      return False
    if len(get_square(board, i)) != 9:
      return False

  return True

def get_row(board, row):
  return to_set(board[row])

def get_col(board, col):
  return to_set(map(lambda row: row[col], board))

def get_square(board, square):
  start_row = square // 3 * 3
  start_col = square % 3 * 3

  res = []
  for row in range(start_row, start_row + 3):
    for col in range(start_col, start_col + 3):
      res.append(board[row][col])

  return to_set(res)

def to_set(row):
  row = set(row)
  row.discard(0)

  return row

print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 7],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True);
                                
print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                         [6, 7, 2, 1, 9, 0, 3, 4, 9],
                         [1, 0, 0, 3, 4, 2, 5, 6, 0],
                         [8, 5, 9, 7, 6, 1, 0, 2, 0],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 0, 1, 5, 3, 7, 2, 1, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False);
