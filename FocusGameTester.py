import unittest

from FocusGame import FocusGame

class FocusGameTester(unittest.TestCase):

    def test_1(self):
        game = FocusGame(('Player1', 'Red'), ('Player2', 'Blue'))
        print(game.move_piece('Player1', (0,0), (0,1), 1))
        print(game.get_board())
        print(game.capture_list('Player1'))
        print(game.show_captured('Player1'))    #0
        print(game.move_piece('Player2', (1,0), (1,1), 1))
        print(game.get_turn())      #Player 1
        print(game.get_next())      # Player 2
        print(game.move_piece('Player1', (0,1), (0,3), 2))
        print(game.move_piece('Player2', (3,5), (3,4), 1))
        print(game.move_piece('Player1', (0,4), (0,3), 1))
        print(game.move_piece('Player2', (4,2), (4,3), 1))
        print(game.move_piece('Player1', (4,4), (4,5), 1))
        print(game.move_piece('Player2', (3,1), (3,2), 1))
        print(game.move_piece('Player1', (4,5), (4,3), 2))
        print(game.move_piece('Player2', (3,4), (3,2), 2))
        print(game.move_piece('Player1', (0,3), (4,3), 4))

        print(game.move_piece('Player2', (2,2), (3,2), 1))
        print(game.move_piece('Player1', (4, 0), (4, 1), 1))
        print(game.move_piece('Player2', (0, 2), (0, 1), 1))
        print(game.move_piece('Player1', (2,0), (2,1), 1))
        print(game.move_piece('Player2', (0,1), (1,1), 1))
        print(game.move_piece('Player1', (1, 2), (1, 1), 1))
        print(game.move_piece('Player2', (3, 2), (5, 2), 2))

        print(game.move_piece('Player1', (4,1), (4,3),2))
        print(game.move_piece('Player2', (1,5), (1,4),1))
        print(game.move_piece('Player1', (0,5), (1,5),1))
        print(game.move_piece('Player2', (5,0), (5,1),1))
        print(game.move_piece('Player1', (5,3), (5,2),1))
        print(game.move_piece('Player2', (1,4), (1,2),2))
        print(game.move_piece('Player1', (5,2), (1,2),4))
        print(game.capture_list('Player1'))    # ['G', 'G', 'G', 'G']
        print(game.show_captured('Player1'))   #4
        print(game.show_reserve('Player1'))    # 2
        print(game.reserve_list('Player1'))    # ['R', 'R']
        print(game.show_pieces((1,2)))         # ['Blue', 'Red', 'Blue', 'Blue', 'Red']


        print(game.move_piece('Player2', (3,2), (0,2),3))
        print(game.move_piece('Player1', (1,3), (1,2),1))
        print(game.move_piece('Player2', (5,1), (3,1),2))
        print(game.move_piece('Player1', (1,5), (1,4),1))
        print(game.move_piece('Player2', (3,1), (1,1),2))
        print(game.get_board())
        print(game.move_piece('Player1', (1,2), (1,1),1))     #player1 Wins




        #print(game.move_piece('Player2', (1, 1), (1, 2), 1))




        #print(game.move_piece('Player2', (0,2), (0,0),2))
        #print(game.reserved_move('Player1', (1, 1)))

        #print(game.move_piece('Player1', (,), (,),))
        # print(game.move_piece('Player2', (,), (,),))
        # print(game.move_piece('Player1', (,), (,),))

        # print(game.move_piece('Player2', (,), (,),))
        # print(game.move_piece('Player1', (,), (,),))


        # print(game.move_piece('Player2', (,), (,),))
        # print(game.show_captured('Player1'))
        # print(game.show_reserve('Player1'))
        # print(game.get_board())

    # def test_2(self):
        # game = FocusGame(('Player1', 'R'), ('Player2', 'G'))
        # print(game.move_piece('Player1', (5,6), (5,5), 1))
        # print(game.move_piece('Player2', (1,5), (1,6), 1))
        # print(game.move_piece('Player2', (1, 5), (1,4), 1))
        # print(game.move_piece('Player3', (1, 5), (1, 4), 1))
        #
        # print(game.move_piece('Player1', (0, 0), (0, 1), 1))
        # print(game.move_piece('Player2', (0, 0), (0, 1), 1))
        # print(game.move_piece('Player2', (2, 1), (0, 1), 1))
        # print(game.move_piece('Player2', (0, 1), (0, 3), 2))
        #
        # # print(game.move_piece('Player1', (,), (,),))
        # print(game.move_piece('Player2', (,), (,),))
        # print(game.move_piece('Player1', (,), (,),))
        # print(game.move_piece('Player2', (,), (,),))
        # print(game.move_piece('Player1', (,), (,),))



        # print('\n')
        # game = FocusGame(('Player1', 'R'), ('Player2', 'G'))
        # print(len(game.show_reserve('Player1')))
        # print(game.move_piece('Player1', (0,0), (0,1), 1))
        # print(game.move_piece('Player2', (0,2), (0,1), 1))
        # print(game.get_board())
        # print(game.reserved_move('Player1', (0,0)))
        # print(game.get_board())
        # print(len(game.show_reserve('Player1')))
        # print(game.show_pieces((0,1)))