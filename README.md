# black-box-game
An abstract board game called Black Box using object-oriented programming principles in Python

You can see the rules [here](https://en.wikipedia.org/wiki/Black_Box_(game)).  It takes place on an 8 x 8 grid.  Rows 0 and 9, and columns 0 and 9 (border squares), are used by the guessing player for shooting rays into the black box.  The atoms are restricted to being within rows 1-8 and columns 1-8.

In this version, the guessing player will start with 25 points.  As stated on the Wikipedia page, "Each entry and exit location counts as a point" that is deducted from the current score. If any entry/exit location of the current ray is shared with any entry/exit of a previous ray, then it should not be deducted from the score again. Each incorrect guess of an atom position will cost 5 points, but repeat guesses should not be deducted from the score again.

There is an online implementation [here](http://www.pythononline.co.uk/blackbox/) that you can try out to get a feel for the game.  It uses different scoring and only allows exactly four atoms (whereas this version allows any number of atoms >= 1).
