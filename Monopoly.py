#Author:    Griffin Sancomb
#Date:  02/09/2020
import pandas as pd

#constants
STARTER_MONEY = 1500


class Player:
    def __init__(self, piece):
        self.piece = piece
        self.money = STARTER_MONEY


def build_board():
    df_board = pd.read_csv("Monopoly_Board.csv")
    print ()
    df_board["Owner"] = None
    df_board.loc[(df_board["Special"] == "site") | (df_board["Special"] == "utility") |
                 (df_board["Special"] == "station"), "Owner"] = "bank"
    print()


# def build_player():
#     print("Enter number of players from 2 - 8")
#     num_players = input("Enter number of players from 2 - 8")
#     players = []
#     for i in range(1, int(num_players)):
#         new_player = Player(input("What piece would you like to be/n"
#                                   "Scottie dog      Top hat     Thimble     Boot/n"
#                                   "Wheelbarrow       Cat     Racing car       Battleship"))
#         players.append(new_player)

def build_player():
    player_df = pd.DataFrame(columns=["piece", "money"])
    num_players = input("Enter number of players from 2 - 8\n")
    for i in range(0, int(num_players)):
        player_piece = input("What piece would you like to be\n"
                             "Scottie dog      Top hat      Thimble       Boot\n"
                             "Wheelbarrow      Cat          Racing car    Battleship\n")
        player_df = player_df.append({"piece": player_piece, "money": STARTER_MONEY},ignore_index=True)
    print()


if __name__ == '__main__':
    #build_board()
    build_player()
