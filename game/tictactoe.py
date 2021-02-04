#Крестики-нолики

import random

def drawBoard(board):
    #Эта функция выводит наэкран поле, клетки которого будут заполняться.

    #"board" - это список из 10 строк, для прорисовки игрового поля
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerletter():
    # Разрешение игроку ввести букву, которую он выбирает
    #ВОзвращает список где первый элемент человек второй комп
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('X O')
        letter = input().upper()

    # Первым элементом списка является буква игрока, вторым — буква компьютера.
    if letter == 'X':
        return ['X', 'O']
    return ['O', 'X']

def whoGoesFirst():
    # Случайный выбор игрока, который ходит первым.
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    return 'Человек'



def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
# Учитывая заполнение игрового поля и буквы игрока, эта функция возвращает True, если игрок выиграл.
 # Мы используем "bo" вместо "board" и "le" вместо "letter", поэтому нам не нужно много печатать.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # через центр
    (bo[1] == le and bo[2] == le and bo[3] == le) or # через низ
    (bo[7] == le and bo[4] == le and bo[1] == le) or # вниз по левой стороне
    (bo[8] == le and bo[5] == le and bo[2] == le) or # вниз по центру
    (bo[9] == le and bo[6] == le and bo[3] == le) or # вниз по правой стороне
    (bo[7] == le and bo[5] == le and bo[3] == le) or # по диагонали
    (bo[9] == le and bo[5] == le and bo[1] == le)) # по диагонали

def getBoardCopy(board):
    # Создает копию игрового поля и возвращает его.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # Возвращает True, если сделан ход в свободную клетку.
    return board[move] == ''

def getPlayerMove(board):

    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход? (1-9)')
        move = input()
    return int(move)

def chooseRandomFromList(board, moveList):
    # Возвращает допустимый ход, учитывая список сделанных ходов и список заполненных клеток.
    # Возвращает значение None, если больше нет допустимых ходов.
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    return None


def getComputerMove(board, computerLetter):
# Учитывая заполнение игрового поля и букву компьютера, определяет допустимый ход и возвращает его.
    if computerLetter == 'X':
        playerletter = 'O'
    else:
        playerletter = 'X'

# Это алгоритм для ИИ "Крестиков-Ноликов":
# Сначала проверяем — победим ли мы, сделав следующий ход.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Проверяем — победит ли игрок, сделав следующий ход, и блокируем его.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerletter, i)
            if isWinner(boardCopy, playerletter):
                return i

    # Пробуем занять один из углов, если есть свободные.
    move = chooseRandomFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Пробуем занять центр, если он свободен.
    if isSpaceFree(board, 5):
        return 5

    # Делаем ход по одной стороне.
    return chooseRandomFromList(board, [2, 4, 6, 8])

def isBoardFull(board):

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Игра "Крестики-нолики"')

while True:
    # Перезагрузка игрового поля
    theBoard = [''] * 10
    playerletter, computerLetter = inputPlayerletter()
    turn = whoGoesFirst()
    print('' + turn + ' ходит первым.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':
            # Ход игрока.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerletter, move)

            if isWinner(theBoard, playerletter):
                drawBoard(theBoard)
                print('Ура! Вы выиграли!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Компьютер'

        else:
            # Ход компьютера.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Компьютер победил! Вы проиграли.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Человек'

    print('Сыграем еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
