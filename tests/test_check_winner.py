import unittest
from models.board import Board

class TestBoard(unittest.TestCase):

    def test_check_winner_rows(self):
        board = Board()
        board.board = [["X", "X", "X"], ["O", " ", " "], [" ", " ", " "]]
        self.assertEqual(board.check_winner(), "X")

    def test_check_winner_columns(self):
        board = Board()
        board.board = [["O", " ", " "], ["O", " ", " "], ["O", "X", " "]]
        self.assertEqual(board.check_winner(), "O")

    def test_check_winner_diagonals(self):
        board = Board()
        board.board = [["X", " ", "O"], [" ", "X", " "], ["O", " ", "X"]]
        self.assertEqual(board.check_winner(), "X")

    def test_no_winner(self):
        board = Board()
        board.board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        self.assertIsNone(board.check_winner())

if __name__ == "__main__":
    unittest.main()
