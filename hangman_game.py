def hangman(code):
    if len(code) < 1 or not code.isalpha():
        print("Please enter a valid word with at least 1 letter.")

    display=["_"] *len(code) #This is the display that will show the player how many letters are in the secret word
    guessed_letters=[]
    lives=6 #This is the number of lives the player has
    while lives > 0 and "_" in display:
        " ".join(display)
        guess=input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
        elif guess in guessed_letters:
            print("You have already guessed that letter. Please try again.")
        elif guess in code:
            print("You guessed a letter correctly!")
            for j in range(len(code)):
                if code[j]==guess:
                    display[j]=guess
            print(display)
        else:
            guessed_letters.append(guess)
            lives-=1
            print("WRONG! You have " + str(lives) + " lives left.")
            stage(lives)
    if "_" not in display:
        print(" ".join(display))
        print("You win! The word was " + code + ".")
    else:
        print("AHH! YOU LOSE!")
        print("The word was " + code + ".")
        
def stage(lives):
    if lives==6: #stage 0:empty gallows(6 lives left)
        print(  """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """)
    elif lives==5: #stage 1:head (5 lives left) 
        print(  """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """
        )
    elif lives==4: #stage 2: body(4 lives left)
        print( """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """)
    elif lives==3: #stage 3: left arm(3 lives left)
        print( """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """)
    elif lives==2: #stage 4: right arm(2 lives left)
        print( """
      +---+
      |   |
      O   |
     /|\\ |
          |
          |
    =========
    """)
    elif lives==1: #stage 5: left leg(1 life left)
        print( """
      +---+
      |   |
      O   |
     /|\\ |
     /    |
          |
    =========
    """)
    elif lives==0: #stage 6: right leg game over 
        print("GAME OVER! You have run out of lives.")
        print( """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """)

    
    
secret_word=input("Enter the secret word: ") #This is the word that the player will try to guess
print("\n"*30) #This is to clear the screen so that the player cannot see the secret word
hangman(secret_word.lower())
