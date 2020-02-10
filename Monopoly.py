# Author:    Griffin Sancomb
# Date:  02/09/2020
import pandas as pd


# constants ints
STARTER_MONEY = 1500
DEFUALT_MULTI_UTIL = 2
ADV_MULTI_UTIL = 10


# constants str
NO_OWNERSHIP = "You dont own any"


class Player:
    def __init__(self, piece):
        self.piece = piece
        self.money = STARTER_MONEY
        # self.sites = [][]
        # self.station = []
        # self.utilities = []
        #


def build_board():
    df_board = pd.read_csv("Monopoly_Board.csv")
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
    player_df = pd.DataFrame(columns=["piece", "money", "site", "station", "utilities"])
    num_players = input("Enter number of players from 2 - 8\n")
    for i in range(0, int(num_players)):
        player_piece = input("What piece would you like to be\n"
                             "Scottie dog      Top hat      Thimble       Boot\n"
                             "Wheelbarrow      Cat          Racing car    Battleship\n")
        player_df = player_df.append({"piece": player_piece, "money": STARTER_MONEY, "site": NO_OWNERSHIP,
                                      "station": NO_OWNERSHIP, "utilities": NO_OWNERSHIP}, ignore_index=True)
    print()
    

def build_cards():
    chance_df = pd.DataFrame(columns=["Description", "amount", "type", "tile", "house", "hotel"])
    chest_df = pd.DataFrame(columns=["Description", "amount", "type", "house", "hotel"])



if __name__ == '__main__':
    build_board()
    build_player()
    build_cards()