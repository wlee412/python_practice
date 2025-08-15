import random

HANGMANPICS = [
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

word_list = ["hamburger","banana","rose","pencil","dog","car"]

selected_word = random.choice(word_list)
letters = list(selected_word)
lives = 0
hearts = 6

placeholder = ["_"]*len(letters)
word = "".join(placeholder)
print(word)

def display(placeholder, user_input):
    if user_input in letters:
        for num in range(len(letters)):
            if letters[num] == user_input:
                placeholder[num] = user_input
    return placeholder

while lives <= 5:
    
    user_input = input("Guess a letter.").strip().lower()
    if user_input in letters:
        print(HANGMANPICS[lives])
        print(f"****************************{hearts}/6 LIVES LEFT****************************")
        placeholder = display(placeholder, user_input)
        word = "".join(placeholder)
        print(word)
        print("a letter you input is exist. :)")
        if letters == placeholder:
            print("You win!!!!!!")
            break
    elif lives == 6:
        print(HANGMANPICS[lives])
        print(f"****************************{hearts}/6 LIVES LEFT****************************")
        print("Game Over.")
        break
    else:
        lives += 1 
        hearts -= 1
        print(HANGMANPICS[lives])
        print(f"****************************{hearts}/6 LIVES LEFT****************************")
        print("a letter does not exist!")    


