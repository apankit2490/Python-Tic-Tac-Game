import numpy as np

class TicTac:
    def __init__(self):
        self.BOARD= [[0,0,0]for count in range(3)]
        self.EMPTY=0
        self.X=1
        self.O=-1
        self.PLAYER=self.X
        self.game_status=False

    def make_a_move(self,x,y):
        if(x<0 or x>2 or y<0 or y>2):
            print("Invalid Position")
            return
        if(self.BOARD[x][y]!=self.EMPTY):
            print("Position already occupied")
            return
        else:
            self.BOARD[x][y]=self.PLAYER
            self.PLAYER=-self.PLAYER

    def display_board(self):
        board_display=""
        for i in range(0,3):
            for j in range(0,3):
                if(self.BOARD[i][j]==self.X):
                    board_display+=" X "
                elif(self.BOARD[i][j]==self.O):
                    board_display+=" O "
                elif(self.BOARD[i][j]==self.EMPTY):
                    board_display+="   "
                    self.game_status=True
                if(j<2):
                    board_display+="|"
            if(i<2):
                board_display+="\n-----------\n"
        print(board_display)

    def print_result(self,sum):
        if(sum==3):
            print("X WON")
            self.game_status=False
            exit(0)
        elif(sum==-3):
            print("O Won")
            self.game_status = False
            exit(0)
        elif (str(0) not in (''.join(str(element) for index in self.BOARD for element in self.BOARD))):
            print("Its a tie")
            exit(0)


    def display_winner(self):
        total=[sum(i) for i in self.BOARD]
        for row_sum in total:
            self.print_result(row_sum)
        total=[sum(i) for i in zip(*self.BOARD)]
        for row_sum in total:
            self.print_result(row_sum)
        numpy_array=np.asarray(self.BOARD)
        diagonal_sum=np.trace(numpy_array)
        self.print_result(diagonal_sum)
        anti_diagonal_sum=np.trace(np.fliplr(numpy_array))
        self.print_result(anti_diagonal_sum)


if __name__=='__main__':
    game=TicTac()

    while(True):
        print("Player X turn" if (game.PLAYER==game.X) else "Player O turn")
        try:
            x=int(input("Enter X place"))
            y =int(input("Enter Y place"))
            game.make_a_move(x,y)
            print(game.BOARD)
            game.display_board()
            print("\n--------------------------------\n")
            game.display_winner()
            if(game.game_status!=True):
                break
        except ValueError:
            print("Enter correct value for place")


