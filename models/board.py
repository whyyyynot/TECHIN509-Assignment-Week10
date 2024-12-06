class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 board

    def draw_board(self):
        for i, row in enumerate(self.board):
            # Add vertical bars at the start and end for symmetry
            print("| " + " | ".join(row) + " |")

            # Print a separator line after the first and second row only
            if i < 2:
                print("-----------")
