class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)
