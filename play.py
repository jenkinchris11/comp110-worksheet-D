import pygame

import oxo


# Initialise PyGame
pygame.init()
clock = pygame.time.Clock()

# Constants
black = (0, 0, 0)
white = (255, 255, 255)
blue = (100, 100, 255)
red = (255, 100, 100)
purple = (200, 0, 255)

window_width = 600
window_height = 600
window_size = (window_width, window_height)

grid_width = 3
grid_height = 3

square_width = window_width / grid_width
square_height = window_height / grid_height

# Create the screen
screen = pygame.display.set_mode(window_size)

# Create the game board
game_board = oxo.OxoBoard()

# If the game is over, game_over_text will be a pygame surface containing the game over text
# Otherwise it will be None
game_over_text = None


def check_game_over():
	""" Check if the game has ended; if so, set game_over_text.
		Return True if the game is over, otherwise False. """
	global game_over_text

	winner = game_board.get_winner()
	if winner != 0:
		font = pygame.font.Font(None, 60)
		game_over_text = font.render("Player %i wins!" % winner, True, purple, white)
		return True
	elif game_board.is_board_full():
		font = pygame.font.Font(None, 60)
		game_over_text = font.render("It's a draw!", True, purple, white)
		return True
	else:
		return False


def draw_board():
	# Clear the screen
	screen.fill(white)

	# Draw the grid lines
	for x in xrange(1, grid_width):
		pygame.draw.line(screen, black, (x * square_width, 0), (x * square_width, window_height), 3)
	for y in xrange(1, grid_height):
		pygame.draw.line(screen, black, (0, y * square_height), (window_width, y * square_height), 3)

	# Draw the board
	for x in xrange(grid_width):
		for y in xrange(grid_height):
			square_contents = game_board.get_square(x, y)
			rect = pygame.Rect((x + 0.2) * square_width, (y + 0.2) * square_height, 0.6 * square_width, 0.6 * square_height)
			if square_contents == 1:
				pygame.draw.ellipse(screen, blue, rect, 3)
			elif square_contents == 2:
				pygame.draw.line(screen, red, rect.topleft, rect.bottomright, 3)
				pygame.draw.line(screen, red, rect.topright, rect.bottomleft, 3)
	

# Main loop
game_is_over = False
current_player = 1
while not game_is_over:
	draw_board()
	pygame.display.flip()
	
	# Handle events, waiting for player to play a move
	played_move = False
	while not played_move:
		event = pygame.event.wait()
		if event.type == pygame.QUIT:
			raise KeyboardInterrupt()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = event.pos
			square_x = mouse_x / square_width
			square_y = mouse_y / square_height
			if game_board.set_square(square_x, square_y, current_player):
				played_move = True
				current_player = 3 - current_player
			else:
				print "Illegal move"
	
	# Check if game is over
	winner = game_board.get_winner()
	if winner != 0:
		game_over_text = "Player %i wins!" % winner
		game_is_over = True
	elif game_board.is_board_full():
		game_over_text = "It's a draw!"
		game_is_over = True
	
	if game_is_over:
		draw_board()
		
		# Draw text in the centre of the screen
		font = pygame.font.Font(None, 60)
		text_surface = font.render(game_over_text, True, (0, 0, 0))
		x = (window_width - text_surface.get_width()) * 0.5
		y = (window_height - text_surface.get_height()) * 0.5
		screen.blit(text_surface, (x, y))
		
		pygame.display.flip()

# Game is over -- wait for user to close the window
while True:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		break
