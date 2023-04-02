stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# You can add your own words here.                                                                  
word_list = [
  "monitor",
  "bed",
  "laptop",
  "chair",
]                                                                    
#imports modules 
#for personal revision
import random


print(logo) #the art of the project
game_is_finished = False    #A boolean variable that later under a certain condition will be true
lives = len(stages) - 1 #it will always equal to 6

chosen_word = random.choice(word_list) #chooses a word from the list of words
word_length = len(chosen_word)

display = []
for _ in range(word_length): #creates blank spaces for the word that is chosen
    display += "_"

while not game_is_finished:    #while the game is not finished do this - all at this indentation gets looped
    guess = input("Guess a letter: ").lower()  

    if guess in display:      #if the letter that you gueesed is already there it tells you and you don't lose a life.
        print(f"You've already guessed {guess}")
#the variable position it is created by this for loop, it is going to give us a number in whitch word it is working with
    for position in range(word_length):  #this for loop is looping through range of the word length whiout the last number
        letter = chosen_word[position] #- letter equals to the chosen word and the position to get the right word out of it  #because the range function is like that
        if letter == guess:  #si la letra es igual al input de guess 
            display[position] = letter   #replaces the _ in display -----> look at variables like that in python.
    print(f"{' '.join(display)}")  #joins the list into a string

    if guess not in chosen_word:   #if the guessed letter is not in the chosen word then you lose a life. If you lose all lifes then you lose and the game is over
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    if not "_" in display:  #if there is no "_" in the display variable the game is over and you win
        game_is_finished = True #the boolean variable
        print("You win.")

    print(stages[lives])