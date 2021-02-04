import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орёл осёл панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорёк черепаха ястреб ящерица'.split()

def get_RandomWord(manyWord):
  i = random.randint(0, len(manyWord) - 1)
  return manyWord[i]

def get_display(correct, miss, secret):
  print(HANGMAN_PICS[len(miss)])
  print()

  print('Ошибочные слова: ', end=' ')
  for letter in miss:
    print(letter, end=' ')
  print()

  blanks = '_' * len(secret)

  for i in range(len(secret)):
    if secret[i] in correct:
      blanks = blanks[:i] + secret[i] + blanks[i+1:]

  for letter in blanks:
    print(letter, end=' ')
  print()

def getguess(a):
  while True:
    guess = input('Введите букву:')
    guess = guess.lower()
    if len(guess) != 1:
      print('Введите 1 букву: ')
    elif guess in a:
      print('Вы уже вводили эту букву')
    elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
      print('Ты далбаеб? БУКВУ ишак!')
    else:
      return guess

def playAgain():
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')

print('В  И  С  Е  Л  И  Ц  А         made by beka@')
miss = ''
correct = ''
secret = get_RandomWord(words)
gameCum = False

while True:
  get_display(correct, miss, secret)

  guess = getguess(correct + miss)
  if guess in secret:
    correct = correct + guess

    foundLetters = True
    for i in range(len(secret)):
      if secret[i] not in correct:
        foundLetters = False
        break
    if foundLetters:
      print('Поздравляю вы нашли слово: ' + secret)
      gameCum = True

  else:
    miss = miss + guess 
    if len(miss) == len(HANGMAN_PICS) - 1:
      get_display(correct, miss, secret)
      print('Увы ты проиграл \n Не угадано: ' + str(len(miss)) + ' Угадано: ' + str(len(correct)) + ' Слово было: ' + secret)
      gameCum = True

  if gameCum:
    if playAgain():
      miss = ''
      correct = ''
      gameCum = False
      secret = get_RandomWord(words)
    else:
      break




      
    
  






