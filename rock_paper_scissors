import random


class Game():
    def __init__(self):
        self.score = 0

    def user(self):
        name = input("Enter your name: ")
        print(f'Hello, {name}')
        file = open('rating.txt', 'r')
        for line in file:
            if name in line:
                self.score = int(line.split()[1])
        file.close()

    def play(self):
        options = input()
        winning_cases = {
            'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
            'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
            'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
            'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
            'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
            'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
            'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
            'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
            'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
            'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
            'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
            'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
            'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
            'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
            'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
        }
        if not options:
            options = ['rock', 'paper', 'scissors']
            winning_cases = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        else:
            options = [option for option in options.split(',')]
        print('Okay, let\'s start')

        while True:
            user_choice = input()
            cp_choice = random.choice(options)
            if user_choice == '!exit':
                print('Bye!')
                break
            elif user_choice == '!rating':
                print(f'Your rating: {self.score}')
            elif user_choice in options:
                if winning_cases[user_choice] == cp_choice or cp_choice in winning_cases[user_choice]:
                    print(f"Well done. The computer chose {cp_choice} and failed")
                    self.score += 100
                elif user_choice == cp_choice:
                    print(f"There is a draw ({cp_choice})")
                    self.score += 50
                else:
                    print(f"Sorry, but the computer chose {cp_choice}")
            else:
                print('Invalid! Try again.')

ready = Game()
ready.user()
ready.play()
