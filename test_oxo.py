# Do not edit, rename or delete this file!

import pytest
import itertools
import oxo

def compare_board(board, expected):
	""" Check the OXO board against the expected board (given as a 9 element list of 0,1,2) """
	for y in xrange(3):
		for x in xrange(3):
			assert board.get_square(x, y) == expected[y*3 + x]

def test_empty_board():
	board = oxo.OxoBoard()
	compare_board(board, [0]*9)

def test_empty_board_no_winner():
	board = oxo.OxoBoard()
	assert board.get_winner() == 0

@pytest.mark.parametrize("x", range(3))
@pytest.mark.parametrize("y", range(3))
@pytest.mark.parametrize("p", [1,2])
def test_first_move(x, y, p):
	board = oxo.OxoBoard()
	assert board.set_square(x, y, p)
	assert board.get_winner() == 0
	expected = [0] * 9
	expected[y*3 + x] = p
	compare_board(board, expected)

@pytest.mark.parametrize("x1", range(3))
@pytest.mark.parametrize("y1", range(3))
@pytest.mark.parametrize("p1", [1,2])
@pytest.mark.parametrize("x2", range(3))
@pytest.mark.parametrize("y2", range(3))
def test_second_move(x1, y1, p1, x2, y2):
	board = oxo.OxoBoard()
	assert board.set_square(x1, y1, p1)
	assert board.get_winner() == 0
	
	p2 = 3 - p1
	
	if x1 == x2 and y1 == y2:
		assert board.set_square(x2, y2, p2) == False
		assert board.get_winner() == 0
	else:
		assert board.set_square(x2, y2, p2)
		assert board.get_winner() == 0
		expected = [0] * 9
		expected[y1*3 + x1] = p1
		expected[y2*3 + x2] = p2
		compare_board(board, expected)

@pytest.mark.parametrize("x", range(3))
@pytest.mark.parametrize("p", [1,2])
def test_vertical_line(x, p):
	x2 = (x + 1) % 3
	p2 = 3 - p
	
	board = oxo.OxoBoard()
	
	for y in xrange(2):
		assert board.set_square(x, y, p)
		assert board.get_winner() == 0
		
		assert board.set_square(x2, y, p2)
		assert board.get_winner() == 0
	
	assert board.set_square(x, 2, p)
	assert board.get_winner() == p

@pytest.mark.parametrize("y", range(3))
@pytest.mark.parametrize("p", [1,2])
def test_horizontal_line(y, p):
	y2 = (y + 1) % 3
	p2 = 3 - p
	
	board = oxo.OxoBoard()
	
	for x in xrange(2):
		assert board.set_square(x, y, p)
		assert board.get_winner() == 0
		
		assert board.set_square(x, y2, p2)
		assert board.get_winner() == 0
	
	assert board.set_square(2, y, p)
	assert board.get_winner() == p

@pytest.mark.parametrize("p", [1,2])
def test_diagonal_line_1(p):
	p2 = 3 - p
	
	board = oxo.OxoBoard()

	for x in xrange(2):
		assert board.set_square(x, x, p)
		assert board.get_winner() == 0
		
		assert board.set_square(x, (x+1) % 3, p2)
		assert board.get_winner() == 0
	
	assert board.set_square(2, 2, p)
	assert board.get_winner() == p

@pytest.mark.parametrize("p", [1,2])
def test_diagonal_line_2(p):
	p2 = 3 - p
	
	board = oxo.OxoBoard()

	for x in xrange(2):
		assert board.set_square(2-x, x, p)
		assert board.get_winner() == 0
		
		assert board.set_square(2-x, (x+1) % 3, p2)
		assert board.get_winner() == 0
	
	assert board.set_square(0, 2, p)
	assert board.get_winner() == p

@pytest.mark.parametrize("p", [1,2])
def test_fill_board(p):
	board = oxo.OxoBoard()
	
	for x,y in [ (1,1), (0,0), (1,2), (1,0), (2,0), (0,2), (0,1), (2,1) ]:
		assert board.set_square(x, y, p)
		assert board.get_winner() == 0
		assert not board.is_board_full()
		p = 3-p
	
	assert board.set_square(2, 2, p)
	assert board.get_winner() == 0
	assert board.is_board_full()
