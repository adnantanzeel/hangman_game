import random
import stages
words=["python","java","javascript","coding","programming"]
lives=6
chosen=random.choice(words)
print(chosen)
display=[]
for i in range(len(chosen)):
    display+='_'
    print(display)
game_end=False
while not game_end:
    guess_letter=input("enter the letter:").lower()
    for position in range(len(chosen)):
        letter=chosen[position]
        if letter==guess_letter:
            display[position]=guess_letter
    if guess_letter not in chosen:
        lives-=1
        if lives==0:
            game_end=True
            print( "you loss the game ")
    if '_'not in display:
        game_end=True
        print("you win")
    print(stages. stages[lives])