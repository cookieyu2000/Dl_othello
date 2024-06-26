# train.py
from othello.OthelloGame import OthelloGame
from othello.bots.DeepLearning import BOT
# from othello.bots.DeepLearning.Alphainit import BOT

class Human:
    def getAction(self, game, color):
        print('input coordinate:', end='')
        coor = input()
        return (int(coor[1]) - 1, ord(coor[0]) - ord('A'))

BOARD_SIZE = 10

bot = BOT(board_size=BOARD_SIZE)

args = {
    'num_of_generate_data_for_train': 500,
    'epochs': 30,
    'batch_size': 256,
    'verbose': True,
    'patience': 10,
}


# 自我對弈訓練
bot.self_play_train(args)

