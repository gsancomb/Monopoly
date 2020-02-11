# Author:    Griffin Sancomb
# Date:  02/09/2020
import pandas as pd

# constants ints
STARTER_MONEY = 1500
DEFAULT_MULTI_UTIL = 2
ADV_MULTI_UTIL = 10
MAX_PLAYERS = 8
MIN_PLAYERS = 2
NUM_HOUSES = 32
NUM_HOTELS = 8
NUM_CHANCE = 16
NUM_CHEST = 16

# constants str
NO_OWNERSHIP = "You dont own any"

#   constant str questions and valid answers
PLAYER_NUM_QUESTION = "Enter number of players from 2 - 8\n"
PLAYER_PIECE = ["Scottie dog", "Top Hat", "Thimble", "Boot", "Wheelbarrow", "Cat", "Racing car", "Battleship"]
PLAYER_PIECE_QUESTION = "What piece would you like to be\n"


# class Player:
#     def __init__(self, piece):
#         self.piece = piece
#         self.money = STARTER_MONEY
#         # self.sites = [][]
#         # self.station = []
#         # self.utilities = []
#         #


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
def player_choice_list(question, options):
    player_input = ""
    while player_input not in options:
        player_input = input(question << "(" << options << ")" << "\n")
    return player_input


def player_choice_num(question, start, range1):
    player_input = 0
    while start <= player_input <= range1:
        player_input = input(question << "(" << start << " - " << range1 << ")" << "\n")
    return player_input


def build_player():
    make_list_players = []
    player_df = pd.DataFrame(columns=["piece", "money", "site", "station", "utilities"])
    num_players = player_choice_num(PLAYER_NUM_QUESTION, MIN_PLAYERS, MAX_PLAYERS)
    for i in range(0, int(num_players)):
        player_piece = player_choice_list(PLAYER_PIECE_QUESTION, PLAYER_PIECE)
        player_df = player_df.append({"piece": player_piece, "money": STARTER_MONEY, "site": NO_OWNERSHIP,
                                      "station": NO_OWNERSHIP, "utilities": NO_OWNERSHIP}, ignore_index=True)
        make_list_players[i] = player_df
    print()
    return make_list_players


# def build_on_site():
# def buy_site():
# def sell_site():
# def mortgage_site():
# def deal():
#     for i in range()
#
#
# def message():


# def turn_menu():
# ans =""
# while ans:
#     print("Enter the number of the Action you would like to take\n"
#           "(You can take as many as you'd like)\n"
#           "1. Build on a site\n"
#           "2. Buy site\n"
#           "3. Sell site\n"
#           "4. Mortgage Site\n"
#           "5. Make a deal\n"
#           "6. Send a message\n"
#           "7. End turn")
#     ans = input("What would you like to do?")
#
#      if ans == 1:
#     #build_on_site()
# elif ans == 2:
#     # buy_site()
# elif ans == 3:
#     #sell_site()
# elif ans == 4:
#     # mortgage_site()
# elif ans == 5:
#     deal()
# elif ans == 6:
#     message()
# elif ans == 7:
#     return
# else:
#     print("That is not a valid answer")


def build_cards():
    make_chance_df = pd.DataFrame(columns=["Description", "amount", "type", "tile", "house", "hotel"])
    make_chest_df = pd.DataFrame(columns=["Description", "amount", "type", "house", "hotel"])
    return make_chance_df, make_chest_df


if __name__ == '__main__':
    build_board()
    build_player()
    chance_df, chest_df = build_cards()
    print()
