import gym
import gym_chess
import random

from stockfish import Stockfish
stockfish = Stockfish('/usr/games/stockfish')

env = gym.make('Chess-v0')

env.reset()
done = False

total_moves = 0 

while not done: 
    print('-'*50)
    move = random.sample(env.legal_moves, 1) # pick a valid random move
    env.step(move[0]) # play the move
    total_moves += 1
    
    # evaluate the position 
    stockfish.make_moves_from_current_position([move[0]]) 
    eval = stockfish.get_evaluation()['value']

    print(f"Move: {total_moves}: Current evaluation is {float(eval) / 100} \n Position: {stockfish.get_fen_position()}")
    print(stockfish.get_board_visual())

    if total_moves > 150: 
        break 




env.close() 