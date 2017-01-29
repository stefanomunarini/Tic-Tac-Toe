import sys


O_WIN = 0
X_WIN = 1
TIE = 2
UNFINISHED = 3
INVALID_BOARD = 4

def check_board_size(board):
  if len(board) != 9:
    return False
  return True


def check_board_values(board):
  # check that the board only contains accepted values
  ACCEPTED_VALUES = ['X', 'O', '']
  for value in board:
    if value not in ACCEPTED_VALUES:
      return False
  return True


def _get_value_count(board, value):
  return board.count(value)


def check_values_compatibility(board):
  # Check that the number of X equals the number of O or (O + 1)
  # Moreover, check that the number of X is always greater than the
  # number of X
  x_count = _get_value_count(board, 'X')
  o_count = _get_value_count(board, 'O')
  if x_count > o_count + 1 or o_count > x_count:
    return False
  return True


def check_game_status(board, winner):
  x_count = _get_value_count(board, 'X')
  o_count = _get_value_count(board, 'O')
  # Unfinished game:
  # 1) not enough X
  # 2) still no winner and board with empty spaces
  if x_count < 3 or (x_count + o_count < len(board) and not winner):
    return False
  return True


def compare_elements(first, second):
  if first == second:
    return True
  return False


def check_triplet(row, index=0):
  if compare_elements(row[index], row[index + 1]):
    if index == 1:
      return True, row[index]
    return check_triplet(row, index=index + 1)
  return False, None


def get_winner(board):
  for index in range(3):
    row = board[ 3 * index : 3 * (index + 1) ]
    row_winner, winner = check_triplet(row)
    if row_winner:
      return winner

    column = [board[index], board[index + 3], board[index + 6]]
    column_winner, winner = check_triplet(column)
    if column_winner:
      return winner

  diagonal = [board[0], board[4], board[8]]
  diagonal_winner, winner = check_triplet(diagonal)
  if diagonal_winner:
    return winner

  diagonal = [board[2], board[4], board[6]]
  diagonal_winner, winner = check_triplet(diagonal)
  if diagonal_winner:
    return winner


def solution(board):
  board_valid = check_board_size(board) and check_board_values(board) and check_values_compatibility(board)
  if not board_valid:
    return INVALID_BOARD

  winner = get_winner(board)

  board_status = check_game_status(board, winner)
  if not board_status:
    return UNFINISHED

  if not winner:
    # Tie
    return TIE
  else:
    if winner == 'O':
      return O_WIN
    elif winner == 'X':
      return X_WIN
    else:
      # any other result means that we are dealing with an invalid board
      return INVALID_BOARD


if not len(sys.argv) > 1:
  print("\033[91mUsage: python3 leadin_test.py 'X O X X X X O O O'\033[0m")
  print("\033[91mIf you wish to provide empty values in the board, the best way is to pass them to the 'solution' function directly inside of the script.\033[0m")
  sys.exit(0)

print('\033[92m' + str(solution(sys.argv[1].split())) + '\033[0m')
