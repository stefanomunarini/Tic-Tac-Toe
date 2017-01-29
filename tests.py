import unittest

from tictactoe import *

class TestLeadin(unittest.TestCase):

	FIRST_ELEMENT = 'X'
	SECOND_ELEMENT = 'O'

	# X O X
	FIRST_ROW = [FIRST_ELEMENT, SECOND_ELEMENT, FIRST_ELEMENT]

	# X X X
	SECOND_ROW = [FIRST_ELEMENT, FIRST_ELEMENT, FIRST_ELEMENT]

	# O O O
	THIRD_ROW = [SECOND_ELEMENT, SECOND_ELEMENT, SECOND_ELEMENT]

	# X O X 
	# X X X 
	# O O O
	VALID_BOARD = []
	VALID_BOARD.extend(FIRST_ROW)
	VALID_BOARD.extend(SECOND_ROW)
	VALID_BOARD.extend(THIRD_ROW)

	# X O X
	# O X X
	# O X O
	TIE_BOARD = [FIRST_ELEMENT, SECOND_ELEMENT, FIRST_ELEMENT,
				 SECOND_ELEMENT, FIRST_ELEMENT, FIRST_ELEMENT,
				 SECOND_ELEMENT, FIRST_ELEMENT, SECOND_ELEMENT]

	def test_element_comparison(self):
		self.assertFalse(compare_elements(self.FIRST_ELEMENT, self.SECOND_ELEMENT))
		self.assertTrue(compare_elements(self.FIRST_ELEMENT, self.FIRST_ELEMENT))
		
	def test_board_size(self):
		self.assertTrue(check_board_size(self.VALID_BOARD), True)

		too_small_board = self.VALID_BOARD[:-1]
		self.assertFalse(check_board_size(too_small_board), False)
		
		too_big_board = []
		too_big_board.extend(self.VALID_BOARD)
		too_big_board.extend(self.FIRST_ELEMENT)
		self.assertFalse(check_board_size(too_big_board), False)

	def test_row_winner(self):
		first_row_winner, _ = check_triplet(self.FIRST_ROW)
		self.assertFalse(first_row_winner)

		second_row_winner, winner = check_triplet(self.SECOND_ROW)
		self.assertTrue(second_row_winner)
		self.assertEqual(winner, self.FIRST_ELEMENT)

		third_row_winner, winner = check_triplet(self.THIRD_ROW)
		self.assertTrue(third_row_winner)
		self.assertEqual(winner, self.SECOND_ELEMENT)

	def test_board_winner(self):
		self.assertEqual(get_winner(self.VALID_BOARD), self.FIRST_ELEMENT)

	def test_solution(self):
		self.assertEqual(solution(self.VALID_BOARD), 1)

	def test_tie(self):
		self.assertEqual(solution(self.TIE_BOARD), 2)
