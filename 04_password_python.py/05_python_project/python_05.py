import random 
Stages = ['''  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
''', '''  _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / 
    |
jgs_|___''', '''  _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      
    |
jgs_|___''','''  _______
    |/      |
    |      (_)
    |      \|/
    |       
    |      
    |
jgs_|___''','''   _______
    |/      |
    |      (_)
    |       |
    |       
    |      
    |
jgs_|___''', '''  _______
    |/      |
    |      
    |      
    |       
    |      
    |
jgs_|___''']
word_list = [ 'nandani', 'pandey','electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop',
'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 
'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 
'bodyguard', 'titanic', 'global', 'ozone', 'bridge']

lives = 6

print('''88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  
                                    aa,    ,88                                
                                    "Y8bbdP"  
            
8b,dPPYba,   
88P'   `"8a  
88       88  
88       88  
88       88  ''')

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = [ ]

while not game_over:
    print(fr
        "******************{lives}/6 LIVES LEFT******************")
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. YOU lose a life")

        if lives == 0:
            game_over = True
            print("******************YOU LOSE******************")

    if "_" not in display:
        game_over = True
        print("******************YOU WIN!******************")

print(Stages[lives])
