class OxoBoard:
    
    
    
   
class OxoBoard
    grid = None
    num_rows = 3 #Three rows
    num_cols = 3  # Three Collumns
    win_row = 3 # number of X an O in a row to win
  

    def __init__(self, num_rows=3, num_cols=3, win_row=3):
        """ The initialiser. Initialise any fields you need here. """
        
        #initialise Variables
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.win_row = win_row
        
        #grid
        self.grid = [[0 for y in xrange(self.num_rows)] for x in xrange(self.num_cols)]
        
        raise NotImplementedError("TODO: implement __init__")

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return.self.grid[X][Y]
        

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.grid[X][Y] == self.empty;
            self.grid[X][Y] = mark
        

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        for x in xrange(self.grid_rows):
            for y in xrange(self.grid_cols):
                
                if self.grid[X][Y] == self.empty:
                    return False
        return true
    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        raise NotImplementedError("TODO: implement get_winner")

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in xrange(3):
            if y > 0:
                print "--+---+--"
            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print
