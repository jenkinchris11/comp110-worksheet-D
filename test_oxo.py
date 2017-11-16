# Do not edit, rename or delete this file!

import pytest
import oxo

def test_empty_board_no_winner():
	board = oxo.OxoBoard()
	assert board.get_winner() == 0

