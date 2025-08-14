import random

word_list = ["hamburger","banana","rose","pencil","dog","car"]

selected_word = random.choice(word_list)
letters = list(selected_word)
lives = 6


print(selected_word)
placeholder = ["_"]*len(letters)
word = "".join(placeholder)
print(word)

def display(placeholder, user_input):
    if user_input in letters:
        for num in range(len(letters)):
            if letters[num] == user_input:
                placeholder[num] = user_input
    return placeholder

while lives >= 0:
    user_input = input("Guess a letter.").strip().lower()
    if user_input in letters:
        placeholder = display(placeholder, user_input)
        word = "".join(placeholder)
        print(word)
        print("a letter you input is exist. :)")
        if letters == placeholder:
            print("You win!!!!!!")
            break
    elif lives == 0:
        print("Game Over.")
        break
    else:
        lives -= 1
        print("a letter does not exist!")    


