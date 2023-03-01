# Author: Jennifer Hoang
# Date: 08/05/20
# Description: The program plays an abstract board game called Black Box.  It takes place on a 10 x 10 grid.
# Atoms are placed in the boxes and another player shoots rays into the black box to guess where the atoms are.

class BlackBoxGame:
    """Plays an abstract board game called Black Box."""

    def __init__(self, atom_pos):
        """Initializes a list of tuples for the locations of the atoms in the black box and any data members."""
        self._board = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]
        self._atom_pos = atom_pos
        self._atoms_left = len(atom_pos)
        self._score = 25
        self._shots = []
        self._guesses = []
        for x in self._atom_pos:
            self._board[x[0]][x[1]] = 'x'

    def print_board(self):
        """Prints out the board for testing."""
        for i in self._board:
            for j in i:
                print(j, " ", end = '')
            print()

    def shoot_ray(self, row, column):
        """Represents the row and column of the border square where the ray originates."""
        if (row == 9 or row == 0) or (column == 0 or column == 9): # Separate border vs non-border.

                if (row == 9 or row == 0) and (column == 0 or column == 9): # This is a border, separate corner vs non-corner.
                    return False

                check_existed = (row, column) in self._shots # Check if shot has been taken.
                if not check_existed:
                    self._shots.append((row, column))
                    self._score -= 1

                for i in self._atom_pos: # This is not the corner, if we hit any atom.
                    if i[0] == row or i[1] == column:
                        return None # Return none if there was a hit.

                if column == 9 or column == 0: # If all atoms are missed, separate between upper and bottom border vs left and right border.
                    column = 9 - column
                else:
                    row = 9 - row

                if not check_existed: # If entry isn't in self._shots, exit gets appended too.
                    self._shots.append((row, column))
                return (row, column)

        return False # This is not a border.

    def guess_atom(self, row, column):
        """Checks if an atom is at the guessed location."""
        if (row, column) in self._guesses: # Already been guessed before.
            if (row, column) in self._atom_pos:
                return True
            else:
                return False
        else: # If this hasn't been guessed before.
            self._guesses.append((row, column))
            if (row, column) in self._atom_pos:
                self._atoms_left -= 1
                return True
            else:
                self._score -= 5
                return False

    def get_score(self):
        """Returns current score."""
        return self._score

    def atoms_left(self):
        """Returns the number of atoms that haven't been guessed yet."""
        return len(self._atom_pos)

# Test code.
game = BlackBoxGame([(3, 2), (1, 7), (4, 6), (8,8)])
game.print_board()
move_result = game.shoot_ray(3,9)
game.shoot_ray(1,2)
game.shoot_ray(0,2)
print(move_result)
print(game.shoot_ray(3, 9), "3 9")
print(game.shoot_ray(3, 0), "3 0")
print(game.shoot_ray(9, 3), "9 3")
print(game.shoot_ray(0, 3), "0 3")
print(game.shoot_ray(4, 0), "4 0")
guess_result = game.guess_atom(5,5)
print(guess_result)
score = game.get_score()
print(score)
atoms = game.atoms_left()