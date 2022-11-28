from aiogram import types
from random import random
import model
from bot import bot


async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'Смысл этой игры: вы с ботом по очереди берете конфеты. Можно за один раз взять от 1 до 28 конфет. Кто возьмет последние конфеты, тот победил')

async def start(message: types.Message):
    model.setCount(int(model.getUserCount()))
    await bot.send_message(message.from_user.id, f'Привет,  {message.from_user.username},\n это игра в конфетки' 
                                                f'чтобы узнать правила, введите команду /help')
    model.setFirstTurn()
    first_step = model.setFirstTurn()
    if first_step:
        await userMove(message)
    else:
        await enemyTurn(message)
async def set_count(message: types.Message):
    count = message.text.split()
    if len(count) == 2:
        model.setUserCount(int(count[1]))
    await bot.send_message(message.from_user.id, f'Стартовое количество конфет изменено, на {model.getUserCount()}')

async def userMove(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.username}, берите конфеты (не больше 28)')
async def playerTurn(message: types.Message):
    move = None
    if message.text.isdigit():
        if int(message.text) < 0 or int(message.text) > 28:
            await bot.send_message(message.from_user.id, f'Нельзя брать больше 28 конфет !')
        else:
            move = int(message.text)
            model.setMove(int(message.text))
            model.setCount(model.getCount() - move)
            await bot.send_message(message.from_user.id, f'{message.from_user.username} взял {move} конфет, на столе осталось {model.getCount()}')
            if model.checkWin():
                await bot.send_message(message.from_user.id, f'Вы выиграли !')
                return
            await enemyTurn(message)
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.username}, введите число')

async def enemyTurn(message: types.Message):
    count = model.getCount()
    move = count%29 if count%29 != 0 else random.randint(1,28)
    model.setMove(move)
    model.setCount(count - move)
    await bot.send_message(message.from_user.id, f'Ход бота:  {model.getMove()} конфет, на столе осталось {model.getCount()}')
    if model.checkWin():
        await bot.send_message(message.from_user.id, f'Бот выиграл !')
        return
    await userMove(message)


async def finish(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'Вы вышли из игры. Сыграем ещё?')

async def getNumber(message: types.Message):
    number = message.text
    if 0 < int(number) < 29:
        print(number)
    else:
        await bot.send_message(message.from_user.id, 'Ах, ты грязный читер!')