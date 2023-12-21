# Princess May Giron
# 232869
# September 28, 2023
# I have not discussed the Python language code in my program
# with anyone other than my instructor or the teaching assistants
# assigned to this course.
# I have not used Python language code obtained from another student,
# or any other unauthorized source, either modified or unmodified.
# If any Python language code or documentation used in my program
# was obtained from another source, such as a textbook or website,
# that has been clearly noted with a proper citation in the comments
# of my program.

import random
import math



def menu(activateHangman):
  
  if activateHangman:
     enableHangman= "2. Disable hangman"
  else:
     enableHangman = "2. Enable hangman"

  print("Welcome to hangman. What do you want to do?")
  print("1. Change number of guesses")
  print(enableHangman)
  print("3. Start game")
  print("4. Quit")
  print()

def playAgain():
    print("Enter RANDOM if you want to guess a random word and QUIT if you want to quit to menu. Meanwhile, you can also enter a word that you'd like to guess.")
    playAgain = input()
    run = False
    if playAgain != "QUIT":
      run = True      
    else:
      run = False
      playAgain = ''
    return run, playAgain

def game():

  ALPHABET = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  randomWords = ['engkanto', 'kapre', 'mangkukulam', 'mambabarang', 'tiktik', 'aswang', 'kidnapper', 'panday', 'gojo', 'geto']
  guesses = 6
  run = True
  activateHangman = False
  
  print("""                                                                                                    
,--.  ,--.  ,---.  ,--.  ,--. ,----.   ,--.   ,--.  ,---.  ,--.  ,--.     ,----.     ,---.  ,--.   ,--.,------. 
|  '--'  | /  O  \ |  ,'.|  |'  .-./   |   `.'   | /  O  \ |  ,'.|  |    '  .-./    /  O  \ |   `.'   ||  .---' 
|  .--.  ||  .-.  ||  |' '  ||  | .---.|  |'.'|  ||  .-.  ||  |' '  |    |  | .---.|  .-.  ||  |'.'|  ||  `--,  
|  |  |  ||  | |  ||  | `   |'  '--'  ||  |   |  ||  | |  ||  | `   |    '  '--'  ||  | |  ||  |   |  ||  `---. 
`--'  `--'`--' `--'`--'  `--' `------' `--'   `--'`--' `--'`--'  `--'     `------' `--' `--'`--'   `--'`------' 
                                          
                                          PREPARE TO GET HANGED                                                                                                
        """)
  while run:
    menu(activateHangman)
    answer = int(input("Enter menu number: "))
    if answer == 1:       
         if activateHangman:
            guesses = int(input("Input number of guesses (min:4, max:10):"))
            if guesses >= 4 and guesses <=10:
               print(f"Sucessfully changed guesses to {guesses}")
            else:
               while guesses < 4 or guesses > 10:
                  guesses= int(input("Number invalid. Input a number again between 4 and 10:"))
               print(f"Sucessfully changed guesses to {guesses}")
         else:
            guesses = int(input("Input number of guesses: "))
            print(f"Sucessfully changed guesses to {guesses}")      
    elif answer == 2:
       
       if activateHangman == False:
          if guesses >=4 and guesses <= 10:
             activateHangman = True
          else:
             while guesses <4 or guesses > 10:
                guesses = int(input("For the guesses, please only input a number between 4 and 10: "))
             print(f"Successfully changed guesses to {guesses}.")
             activateHangman = True
          
       else:
          activateHangman = False
    elif answer== 3:
      
      runGame = True      
      while runGame:
        word = ''
        hangman(guesses, randomWords, ALPHABET, word, activateHangman)
        
        while word != "QUIT":
           runGame, word = playAgain()
           
           if word != "" and word != "RANDOM":
              
              process(word, guesses,activateHangman)
           elif word == "RANDOM":
              
              randomWord(randomWords, guesses, activateHangman)
           else:
              
              runGame= False
              break
    else:
       
       break


def hangmanPics(guess, wrongGuesses):
  
  wGuess = wrongGuesses
  fourGuesses = [
  '''
    +---+
    |   |
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''',

  '''
    +---+
    |   |
    |   |
    x   |
   /|\  |
   / \  |
        |
  =========
  '''
  ]
  fiveGuesses = [
  '''
    +---+
    |   |
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''',

  '''
    +---+
    |   |
    |   |
    x   |
   /|\  |
   / \  |
        |
  =========
  '''
  ]
  sixGuesses = [
  '''
    +---+
    |   |
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''',

  '''
    +---+
    |   |
    |   |
    x   |
   /|\  |
   / \  |
        |
  =========
  '''
  ]
  sevenGuesses = [
  '''
    +---+
    |   |
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''',

  '''
 +---+
    |   |
    |   |
    x   |
   /|\  |
   / \  |
        |
  =========
  '''
  ]
  eightGuesses = [
  '''
    +---+
    |   |
    |   |
        |
        |
        |
        |
  ========='''
  ,'''
    +---+
    |   |
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''',

  '''
   +---+
    |   |
    |   |
    x   |
   /|\  |
   / \  |
        |
  =========
  '''
  ]
  nineGuesses = [
      '''
    +---+
        |
        |
        |
        |
        |
        |
  =========''', 
  '''
    +---+
    |   |
    |   |
        |
        |
        |
        |
  ========='''
  ,'''
    +---+
    |   |
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''',

  '''
    +---+
    |   |
    |   |
    x   |
   /|\  |
   / \  |
        |
  =========
  '''
  ]
  tenGuesses = [
      '''
    






  ========='''

  ,'''
    +---+
        |
        |
        |
        |
        |
        |
  =========''', 
  '''
    +---+
    |   |
    |   |
        |
        |
        |
        |
  ========='''
  ,'''
    +---+
    |   |
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''',

  '''
   +---+
    |   |
    |   |
    x   |
   /|\  |
   / \  |
        |
  =========
  '''
  ] 
  if guess == 4:
     print(fourGuesses[wGuess])
  elif guess == 5:
     print(fiveGuesses[wGuess])
  elif guess == 6:
     print(sixGuesses[wGuess])
  elif guess == 7:
     print(sevenGuesses[wGuess])
  elif guess == 8:
     print(eightGuesses[wGuess])
  elif guess == 9:
     print(nineGuesses[wGuess])
  else:
     print(tenGuesses[wGuess])
  wGuess+=1
  return wGuess

def hyphenize(word):
    hyphen = ''
    hyphenArray = []
    wordCount= 0
    for i in word:
        hyphen+='-'
        hyphenArray.append('-')
        wordCount+=1
    return hyphen, hyphenArray, wordCount

def removeLetter(letter, strA, arrayA):
    j = 0
    pos= 0
    for i in strA:
        if i == letter:
            pos = j
            break
        j+=1
    arrayA[pos] = ''
    strA = ''
    for i in arrayA:
        strA +=i
    return strA

def usedLetters(usedL):
   letter = input("Enter a letter:")
   count = 0
   while letter == "":
      letter = input("Enter a letter:")
   for i in usedL:
      if i ==letter:
         while i == letter:
            letter = input("You already entered that letter. Please enter a different letter: ")
   return letter
      
def process(word, guessCount, showHangman):
        lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
        foundLetter = 0
        wrongGuess = 0
        hyphenated = ''
        hyphenArray = []
        wordCount = 0
        guesses = guessCount
        if word == "":
            word = input("Enter word: ")
        
        hyphenated, hyphenArray, wordCount = hyphenize(word)
        alphabet= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        strAlphabet = alphabet
        wordFound = False      
        usedAlphabets = []

        while guessCount > 0 and wordFound == False:
            print(f"Guess the word, {guessCount} guess(es) left: {hyphenated}")
            print(f"Unused letters: {strAlphabet} \n")
            posL = 0
            posA = 0
            letterFound = False
            k = 0
            upperPosition = 0
            lowerPosition = 0
            posUpper = 0
            posLower = 0
            capitalLetter = ''
            notCapital = ''
            upperBool = True
            lowerBool = False
            letter = usedLetters(usedAlphabets)
            for i in upper:
                if i == letter:
                    posUpper = upperPosition
                    upperBool = True
                    notCapital= lower[posUpper]
                    capitalLetter = i
                    break
                else:
                    upperBool = False
                    lowerBool = True
                upperPosition+=1
            if lowerBool == True:
                for i in lower:
                    if i == letter:
                        posLower = lowerPosition
                        notCapital= i
                        capitalLetter = upper[posLower]
                        break
                
                    lowerPosition+=1
            
            
            for i in word:
                if i == notCapital or i == capitalLetter:
                    posL = k
                    letterFound = True
                    foundLetter +=1
                    if letterFound:
                      hyphenArray[posL] = capitalLetter
                      hyphenated = ""
                    for i in hyphenArray:
                        hyphenated +=i
                k +=1
            
            usedAlphabets += [capitalLetter]
            usedAlphabets += [notCapital]
            strAlphabet =removeLetter(capitalLetter, alphabet, upper)
            if letterFound == False:
                print('This letter is not on the word. \n')
                if showHangman:
                   wrongGuess = hangmanPics(guesses, wrongGuess)
                guessCount -=1

                if guessCount == 0 and letterFound == False:
                    print(f"Guess the word, {guessCount} guess(es) left: {hyphenated}")
                    print(f"Unused letters: {strAlphabet} \n")
                    print("Wrong! Better luck next time! ")
                    print(f"The correct answer is {word}. \n")
                    

            if letterFound == True and wordCount == foundLetter:
              wordFound = True
              
              if showHangman:
                 print("""
          
.-.  .-..---. .-. .-.    .-.  .-..-..-. .-..-. 
 \ \/ // {-. \| } { |    | {  } |{ ||  \{ || | 
  `-\ }\ '-} /\ `-' /    {  /\  }| }| }\  {{ } 
    `-' `---'  `---'     `-'  `-'`-'`-' `-'`-' 
                                                                                                 
                       """)
              
                 print(f"Congrats, you correctly guessed the word: {word}!")
              else:
                 print(f"Guess the word, {guessCount} guess(es) left: {hyphenated}")
                 print(f"Unused letters: {strAlphabet} \n")
                 print(f"Congrats, you correctly guessed the word! You win!\n")
                 
              
            
            letterFound = False
            
def randomNum():
    a = random.random() *10
    return math.floor(a)

def randomWord(randomWords, guessCount, hangmanEnabled):
   process(randomWords[randomNum()], guessCount, hangmanEnabled)

def hangman(guess, randomWords, alphabet, word, hangmanEnabled):

    guessCount = guess    
    alphabet = alphabet
    print("Would you rather..")
    print("1. Enter own word")
    print("2. Use a random word from the database")
    choice = int(input("Enter number: "))
    if choice == 1:
        process(word, guessCount, hangmanEnabled)
    elif choice == 2:
       randomWord(randomWords, guessCount, hangmanEnabled)

game()

