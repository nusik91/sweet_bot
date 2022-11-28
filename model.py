import random
from aiogram import types

user_count = 150
total_count = 150
first_step = None
move = None

def getFirstTurn():
    return first_step
def setFirstTurn():
    global first_step
    first_step = random.randint(0,1)
def getMove():
    global move
    return move
def setMove(new_move: int):
    global move
    move = new_move
def getCount():
    global total_count
    return total_count
def setCount(count: int):
    global total_count
    total_count = count
def getUserCount():
    global user_count
    return user_count
def setUserCount(count: int):
    global user_count
    user_count = count
def checkWin():
    if getCount() <= 0:
        return True
