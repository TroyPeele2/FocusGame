# Author: Troy Peele II
# Date: 11/22/2020
# Description: Class FocusGame represents the entirety of the game domination. The players and board are initiated as
# private data members within the FocusGame Class. Each player also has data members that are specified to each player
# with either a 1 or 2 which represents if that data member refers to player 1 or player 2. The game allows a player to
# make three types of moves on their turn which is either a single move, a multiple move, or a reserve move. The goal
# of the game is for a player to capture 6 pieces of the opposing player's pieces. If the player capture a piece of
# their own it will become a reserve piece for them to play. If a player happens to capture 6 pieces of the opposing
# player, that player will be declared the winner of the game.

class FocusGame:
    '''Class FocusGame represents the entirety of the game domination, which allows two players to play the game
    domination until somebody wins the game.'''

    def __init__(self, player_1, player_2):
        '''Represents the private data members of the game domination. It takes two parameters which are tuples, the
        first being player1 and that players designated color and the second tuple being player2 and their designated
        color.The init method then sets 11  private data members which are, player1, player2, player1 color,
        player2 color, player1 reserve, player2 reserve, player1 capture, player2 capture, the game board which is a
        list of lists from (0,0) to (5,5), whose turn it is, and whose turn is next. The board gets initalized by using
        the player1 and player2 color which are denoted as c1 and c2. This allows each player to choose the color they
        would like to be for the game'''

        self._player1 = player_1[0]
        self._player2 = player_2[0]
        self._color1 = player_1[1]  # added [0] here 11.30
        self._color2 = player_2[1]   # added [0] here 11.30
        c1 = 'R'          # added [0] here 11.30
        c2 = 'G'           # added [0] here 11.30
        self._board_color1 = 'R'
        self._board_color2 = 'G'
        self._reserve1 = []
        self._reserve2 = []
        self._capture1 = []
        self._capture2 = []
        self._board = [[c1, c1, c2, c2, c1, c1], [c2, c2, c1, c1, c2, c2], [c1, c1, c2, c2, c1, c1],
                      [c2, c2, c1, c1, c2, c2], [c1, c1, c2, c2, c1, c1], [c2, c2, c1, c1, c2, c2]]
        self._turn = player_1[0]
        self._next = player_2[0]

    def move_piece(self, name, position, new_spot, move):
        '''Function move_piece as a parameter player name, current piece coordinate, the new spot coordinate, and number
        of pieces to move. The function first validates if the input is valid with the validate function, and if it is
        invalid it returns the appropriate return statement. If the move is valid, it then calls the moving function,
        followed by the stack length function, and last checks if the move has created a win. If the move has caused a
        win then it returns the player wins. If there is no win, then it returns move successful'''

        # if statement calls upon the method validate move to see if the function is not True. If the function doesn't
        # return True then it calls upon and returns the value from validate move.
        if self.validate_move(name, position, new_spot, move) != True:
            return self.validate_move(name, position, new_spot, move)

        # else, call upon the moving function to actual make a move to the board. Following that, call upon the stack
        # length function to check the length of the new coordinate. After call upon check win function to see if that
        # move has made a player win the game. If the move doesn't result in a win, return 'Move Successful'
        else:
            self.moving(name, position, new_spot, move)
            self.stack_length(name, new_spot)
            if self.check_win(name) is not None:
                return self.check_win(name)
            return 'successfully moved'

    def validate_move(self, name, position, new_spot, move):
        '''Function validate_move takes as a parameter player name, current piece coordinate, the new spot coordinate,
        and number of pieces to move. The functions purpose is to validate whether or not the move is valid. This
        function will check to see if the current position of the piece and the new spot that the piece will move is a
        valid index, if it is the users turn, if the position and new spot is a valid or invalid location, if the
        player's pieces to move are valid. If the move meets all the above parameters then it will return True, else it
        will return the corresponding error'''

        # try statement checks to see if the coordinate given is valid. If either the current coordinate or new
        # coordinate raises an index error, the function will returns 'index error'
        try:
            self.get_board()[position[0]][position[1]]
            self.get_board()[new_spot[0]][new_spot[1]]
        except IndexError:
            return False

        # if name of the player isn't the name of player1 and player 2, return 'You're not a player of this game'
        if name != self.get_player1() and name != self.get_player2():
            return False

        # if name of the player isn't the name of the private data member self._turn, then return 'Not your turn'
        if name != self.get_turn():
            return False

        # if the board at the current position is none or the current position coordinate equals the new spot coordinate
        # return invalid location
        if self.get_board()[position[0]][position[1]] == None or position == new_spot:
            return False

        # if the coordinate position[0] and new spot[0] are not equal and coordinate position[1] and new spot[1] are not
        # equal, return 'invalid location'
        if self.get_board()[position[0]] != self.get_board()[new_spot[0]] and self.get_board()[position[1]] != self.get_board()[new_spot[1]]:
            return False

        # if the piece at coordinate position is not equal to the player's color, return 'invalid location'
        if self.get_board()[position[0]][position[1]][-1] != self.get_board_color(name):
            return False

        # if the number of pieces to move is greater than the length of the stack at the board position, return 'invalid
        # number of pieces'
        if move > len(self.get_board()[position[0]][position[1]]):
            return False

        # if the number of pieces to move is less or equal to the length of the stack at the board position,
        if move <= len(self.get_board()[position[0]][position[1]]):

            # if position[0] - new_spot[0] is equal to the number of pieces to move or position[1] - new_spot[1] is
            # equal to the number of pieces to move, return True, else return 'Wrong distance'
            if abs(position[0] - new_spot[0]) == move or abs(position[1] - new_spot[1]) == move:
                return True
            else:
                return False

    def moving(self, name, position, new_spot, move):
        '''Function moving takes as a parameter player name, current position coordinate, the new spot coordinate, and
        number of pieces to move. This functions purpose is to actually make the movement of the pieces on the board. It
        will first check that the pieces to move are equal to the length of the pieces at the original position. If that
        is not the case, then it will see if the pieces to move is less than the length of the pieces at the original
        position. Depending on the number of pieces to move, it will then execute the corresponding statement and return
        successfully moved'''

        # if move is equal to the length of the board at the current coordinate position
        if move == len(self.get_board()[position[0]][position[1]]):

            # if the board at the new spot coordinate is None, that new coordinate stack equals the current position
            # coordinate stack. Then set the current position coordinate equal to None. Then set the turn equal to the
            # name of next player and set the next turn after that equal to the current player name and return
            # 'successfully moved'
            if self.get_board()[new_spot[0]][new_spot[1]] is None:
                self._board[new_spot[0]][new_spot[1]] = self.get_board()[position[0]][position[1]]
                self._board[position[0]][position[1]] = None
                self.set_turn(self.get_next())
                self.set_next(name)

            # else since the board at the new spot coordinate is not None, that new spot coordinate stack equals the new
            # spot coordinate stack + the current position coordinate stack. Then the current position coordinate equals
            # None. Then set the turn equal to the name of next player and set the next turn after that equal to the
            # current player name and return 'successfully moved'
            else:
                self._board[new_spot[0]][new_spot[1]] = self.get_board()[new_spot[0]][new_spot[1]] + \
                                                       self.get_board()[position[0]][position[1]]
                self._board[position[0]][position[1]] = None
                self.set_turn(self.get_next())
                self.set_next(name)

        # else if move is less than the length of the board at the current coordinate position
        elif move < len(self._board[position[0]][position[1]]):

            # if the board at the new spot coordinate is None, that new coordinate stack equals the current position
            # coordinate stack from the index [-move:]. The current position coordinate stack is now equal to the
            # current position coordinate stack from the index [:-move]. Then set the turn equal to the name of next
            # player and set the next turn after that equal to the current player nameand return 'successfully moved'
            if self._board[new_spot[0]][new_spot[1]] is None:
                self._board[new_spot[0]][new_spot[1]] = self.get_board()[position[0]][position[1]][-move:]
                self._board[position[0]][position[1]] = self.get_board()[position[0]][position[1]][:-move]
                self.set_turn(self.get_next())
                self.set_next(name)

            # else since the board at new spot coordinate is not None, that new spot coordinate stack equals the current
            # stack of new spot coordinate + the current position coordinate stack from the index [-move:]. The current
            # position coordinate stack is now equal to the current position coordinate stack from the index [:-move].
            # Then set the turn equal to the name of next player and set the next turn after that equal to the current
            # player name and return 'successfully moved'
            else:
                self._board[new_spot[0]][new_spot[1]] = self.get_board()[new_spot[0]][new_spot[1]] + \
                                                       self.get_board()[position[0]][position[1]][-move:]
                self._board[position[0]][position[1]] = self.get_board()[position[0]][position[1]][:-move]
                self.set_turn(self.get_next())
                self.set_next(name)
        return 'successfully moved'

    def stack_length(self, name, new_spot):
        '''Function stack_length takes as a parameter player name and new_spot coordinate to check the length of stack
        at the new_spot. This function is utilized directly after the moving functions to check the new stack length.
        stack_length uses a while loop that is true as long as the stack length is greater than 5. If the length is
        greater than 5 it determines whether or not the bottom piece will be captured or reserved for that player.'''

        # while loop test to see if the length of the new spot is greater than 5
        while len(self._board[new_spot[0]][new_spot[1]]) > 5:

            # piece represents the 0th index value of the stack
            piece = self.get_board()[new_spot[0]][new_spot[1]][0]

            # if the piece is the same color as the player's designated color, add piece to that player's reserve list
            # and set the value of new spot coordinate equal to itself from [1::]
            if piece == self.get_board_color(name):
                reserve = self.reserve_list(name)
                reserve += piece
                self._board[new_spot[0]][new_spot[1]] = self._board[new_spot[0]][new_spot[1]][1::]

            # if the piece is not the same color as the player's designated color, it is then the opponents color. Add
            # the piece to the player's capture list and set the value of new spot coordinate equal to itself from [1::]
            elif piece != self.get_board_color(name):
                capture = self.capture_list(name)
                capture += piece
                self._board[new_spot[0]][new_spot[1]] = self._board[new_spot[0]][new_spot[1]][1::]

    def reserved_move(self, name, new_spot):
        '''Function reserved_move takes as a parameter name of the player and the new spot coordinate where the piece
        will go. It first uses a try statement to confirm that  new spot is a valid coordinate. It then checks to see if
        it is indeed the players turn, then if the player has reserve pieces. If it passes those initial tests, then it
        calls upon the function reserved_moving to make the actual move. It then calls the stack_length function
        followed by the check_win function. If this does not result in a win, it returns successfully moved. '''

        # try statement checks to see if the new spot coordinate given is valid. If the new coordinate raises an index
        # error, the function will returns 'index error'
        try:
            self.get_board()[new_spot[0]][new_spot[1]]
        except IndexError:
            return False

        # if name of the player isn't the name of the players whose turn it is, then return 'Not your turn'
        if name != self.get_turn():
            return False

        # if the player has an empty reserve list, return 'No pieces in reserve'
        if self.show_reserve(name) == 0:
            return False

        # else call the function reserved_moving to make the actual move. After the move has been made call the
        # stack_length function to check the length. After call the check win function to see if the move results in a
        # win. If it has not resulted in a win return 'successfully moved'
        else:
            reserve_piece = self.reserve_list(name)[0]
            self.reserved_moving(name, reserve_piece, new_spot)
            self.stack_length(name, new_spot)
            if self.check_win(name) is not None:
                return self.check_win(name)
        return 'successfully moved'

    def reserved_moving(self, name, reserve_piece, new_spot):
        '''Function reserved_moving takes as a parameter player name, the reserve piece, and new spot coordinate. The
        function checks the value of the new spot and executes the appropriate statement.'''

        # If the board at the new spot coordinate is None. The new spot coordinate equals the reserve piece. Then remove
        # the piece from the players reserve. Then set turn equal to the name of next player and set the next turn equal
        # to the current player name
        if self.get_board()[new_spot[0]][new_spot[1]] is None:
            self._board[new_spot[0]][new_spot[1]] = reserve_piece
            self.reserve_list(name).pop(0)
            self.set_turn(self.get_next())
            self.set_next(name)

        # Else if the board at the new spot coordinate is not None. The new spot coordinate equals the new spot
        # coordinate value + the reserve piece. Then remove the piece from the players reserve. Then set turn equal to
        # the name of next player and set the next turn equal to the current player name.
        else:
            self._board[new_spot[0]][new_spot[1]] = self.get_board()[new_spot[0]][new_spot[1]] + reserve_piece
            self.reserve_list(name).pop(0)
            self.set_turn(self.get_next())
            self.set_next(name)

    def check_win(self, name):
        '''Function check win takes as a parameter the name of the player to see if the length of the player's captured
        pieces is greater than or equal to 6. If it is then it returns player wins'''

        # if player captured list is greater than or equal to 6, return 'Player Wins'
        if self.show_captured(name) >= 6:
            return name + ' Wins'

    def get_board(self):
        '''Function get_board returns the current layout of the board'''
        return self._board

    def get_color(self, piece):
        '''Function get color takes as a parameter a name and returns the color that the player has chosen'''

        # If the name equals player1 return player1 player1 color. Else if the name equals player2, return player2 color
        if piece == 'R':
            return self._color1
        elif piece == 'G':
            return self._color2

    def get_board_color(self, name):
        '''Function get board color takes as a parameter a name and returns the color that the player has chosen'''

        # If the name equals player1 return player1 player1 color. Else if the name equals player2, return player2 color
        if name == self.get_player1():
            return self._board_color1
        elif name == self.get_player2():
            return self._board_color2

    def reserve_list(self, name):
        '''Function takes as a parameter a name and returns the reserve list for that player.'''

        # If the name equals player1 return player1 reserve list. Else if the name equals player2, return player2
        # reserve list
        if name == self.get_player1():
            return self._reserve1
        elif name == self.get_player2():
            return self._reserve2

    def show_reserve(self, name):
        '''Function show_reserve takes as a parameter a player name and returns the number of pieces that are in
        reserve for that player. If no pieces are in reserve, return 0.'''

        # If the name equals player1 return player1 reserve list length. Else if the name equals player2, return player2
        # reserve list length
        if name == self.get_player1():
            return len(self._reserve1)
        elif name == self.get_player2():
            return len(self._reserve2)

    def capture_list(self, name):
        '''Function takes as a parameter a name and returns the capture list for that player.'''

        # If the name equals player1 return player1 capture list. Else if the name equals player2, return player2
        # capture list.
        if name == self.get_player1():
            return self._capture1
        elif name == self.get_player2():
            return self._capture2

    def show_captured(self, name):
        '''Function show_captured takes as a parameter a player name and returns the number of pieces that are in
        captured for that player. If no pieces are in reserve, return 0.'''

        # If the name equals player1 return player1 capture list length. Else if the name equals player2, return player2
        # capture list length
        if name == self.get_player1():
            return len(self._capture1)
        elif name == self.get_player2():
            return len(self._capture2)

    def show_pieces(self, position):
        '''Function show pieces takes a position coordinate on the board and returns a list that shows the pieces that
        are present at that specified coordinate.'''

        # create an empty list called pieces_list
        pieces_list = []

        # for every piece at the board coordinate, add the piece to the pieces_list then return the list
        for piece in self.get_board()[position[0]][position[1]]:
            true_piece = self.get_color(piece)
            pieces_list.append(true_piece)
        return pieces_list

    def get_turn(self):
        '''Function get_turn returns the name of the player whose turn it currently is'''
        return self._turn

    def set_turn(self, name):
        '''Function set_turn takes as a parameter a name and sets that player name to be whose turn it is'''
        self._turn = name

    def get_next(self):
        '''Function get_next returns the name of the player whose turn is next after the current turn'''
        return self._next

    def set_next(self, name):
        '''Function set_next takes as a parameter a name and sets that player name to be whose turn it will be next
        after turn.'''
        self._next = name

    def get_player1(self):
        '''Function returns the name of player1'''
        return self._player1

    def get_player2(self):
        '''Function returns the name of player2'''
        return self._player2