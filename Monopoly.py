# Author:    Griffin Sancomb
# Date:  02/09/2020
import pandas as pd
import random2 as random
import csv
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
PLAYER_NUM_QUESTION = "Enter number of players from "
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
# Working functions dont touch

def build_board():
    df_board = pd.read_csv("Monopoly_Board.csv")
    df_board["Owner"] = None
    df_board.loc[(df_board["Special"] == "site") | (df_board["Special"] == "utility") |
                 (df_board["Special"] == "station"), "Owner"] = "bank"
    return df_board


def player_choice_list(question, options):
    player_input = None
    while str(player_input) not in str(options):
        player_input = input(str(question) + "(" + str(options) + ")" + "\n")
    return player_input


def player_choice_num(question, start, range1):
    player_input = 0
    while int(player_input) < int(start) or int(player_input) > int(range1):
        player_input = input(question + str(start) + " - " + str(range1) + "\n")
    return player_input


def build_player():
    make_list_players = []
    player_df = pd.DataFrame(columns=["piece", "money", "site", "station", "utilities"])
    num_players = player_choice_num(PLAYER_NUM_QUESTION, MIN_PLAYERS, MAX_PLAYERS)
    for i in range(int(num_players)):
        player_piece = player_choice_list(PLAYER_PIECE_QUESTION, PLAYER_PIECE)
        player_df = player_df.append({"position": "GO", "piece": player_piece, "money": STARTER_MONEY, "site": NO_OWNERSHIP,
                                      "station": NO_OWNERSHIP, "utilities": NO_OWNERSHIP}, ignore_index=True)
        make_list_players.append(player_df)
    return make_list_players


def build_cards():
    with open('ChestCards.csv', 'rt') as file:
        make_chest_read = csv.reader(file)
        chest = list(make_chest_read)
    chest.pop(0)
    with open('ChanceCards.csv', 'rt') as file:
        make_chance_read = csv.reader(file)
        chance = list(make_chance_read)
    chance.pop(0)
    return chance, chest
    # make_chance_df = pd.read_csv("ChanceCards.csv")
    # make_chest_df = pd.read_csv("ChestCards.csv")
    # make_chance_df = pd.DataFrame(columns=["Description", "amount", "type", "tile", "house", "hotel"])
    # make_chest_df = pd.DataFrame(columns=["Description", "amount", "type", "house", "hotel"])
    # return make_chance_df, make_chest_df


# nonworking functions
def shuffle_cards(deck):
    random.shuffle(deck)
    return deck


# def roll_dice():
# def build_on_site():
# def buy_site():
# def sell_site():
# def mortgage_site():
# def deal():
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


def turn_main(board, player_list, index):
    curr_player = player_list[index]
    is_double = True
    double_count = 0
    while is_double:
        # roll dice
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        if dice_one == dice_two:
            double_count += 1
            is_double = True
        else:
            is_double = False
# move player
    # move player(curr_player)
# load tile data
    # curr_tile = tile_data(curr_player[1])
# Collect rent
    # collect_rent()
# call menu
    # turn_menu()


    if double_count >= 3:
        print("Those dice must be loaded. Go straight to jail")
        # got_to_jail()
    #

if __name__ == '__main__':
   # board = build_board()
   # list_of_players = build_player()
    chance_list, chest_list = build_cards()
    chance_list = shuffle_cards(chance_list)
    chest_list = shuffle_cards(chest_list)
    print()
