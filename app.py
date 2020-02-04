import os
import sys
import time
from random import shuffle

# -- Pool of questions and answers respectively --
pool = [
    ['pregunta1', 'respuesta1'],
    ['pregunta2', 'respuesta2'],
    ['pregunta3', 'respuesta3'],
    ['pregunta4', 'respuesta4'],
    ['pregunta5', 'respuesta5'],
    ['pregunta6', 'respuesta6'],
    ['pregunta7', 'respuesta7'],
    ['pregunta8', 'respuesta8'],
    ['pregunta9', 'respuesta9'],
    ['pregunta10', 'respuesta10']
]


class Pool:
    def __init__(self):
        self.items = []
        # -- We create a dictionary with 'Question' and 'Answer' as keys --
        for item in pool:
            question = item[0]
            answer = item[1]
            self.items.append({'question': question, 'answer': answer})

    # -- Checks how many questions there are in the pool --
    def __repr__(self):
        return f'There are {len(self.items)} questions in the pool'

    def shuffle(self):
        shuffle(self.items)

    # -- Display the list of questions in the pool --
    def check_pool(self):
        for pair in self.items:
            print(pair['question'])


class Format:
    def __init__(self, question):
        self.question = question
        # self.answer = answer

    # -- Provies the format to the questions --
    def __repr__(self):
        return f'The question you need to answer is: {self.question}'


# -- Main Class --
class Game(Pool):
    def __init__(self, class_pool, i=0):
        super().__init__()
        self.i = i
        self.items = class_pool.items
        self.score = 0
        self.total_score = 0

    # -- Get the questions from the dictionary and calls to Format to print them.  --
    # -- Then it calls to Game.attempt to start the attempts --
    # -- This takes into account the number of questions the user wants to answer [i] --
    def get_question(self):
        for i in range(0, self.i):
            question = (self.items[i]['question'])
            print(Format(question))
            Game.attempt(self, i)
            if i < self.i - 1:
                stop = input(f'Do you want to continue? Y/N: ')
                stop = stop.lower()
                Menu.safe_quit(stop)
                os.system('cls')
            elif i == self.i - 1:
                stop = 'n'
                Menu.safe_quit(stop)

    # -- Checks if the answer is correct and adds points to the main score --
    def attempt(self, question):
        question = question
        correct_answer = self.items[question]['answer']
        user_answer = input('\nPlease enter your answer: ')
        user_answer = user_answer.lower()
        # -- Check if the answer is correct or not. Returns score --
        if user_answer == correct_answer:
            self.score = self.score + 1
            print(f'\nCongrats, that\'s the correct answer. Your score is {self.score}.\n')
            return self.score
        else:
            print(f'\nI\'m sorry, that\'s not correct. Your score is  {self.score}.\n')

    @staticmethod
    def final_score(score):
        total_score = (score / play.i) * 100
        return total_score


# -- Creates the user menu --
class Menu:
    @staticmethod
    def options():
        print(f'Press "1" to check how many questions there are in the pool')
        print(f'Press "2" to check the questions in the pool')
        print(f'Press "3" to start the game')
        print(f'Press "Q" to quit.\n')
        user_choice = input()
        user_choice = user_choice.lower()
        return user_choice

    # -- If the user don't want to answer more questions he can quit.
    @staticmethod
    def safe_quit(stop):
        stop = stop
        if stop == 'y':
            pass
        else:
            print(f'Thanks for playing')
            print(f'Your total score is {play.score} out of {play.i}.')
            print(f'which is equivalent to {Game.final_score(play.score)} out of 100.')
            sys.exit(0)

    # -- Game Rules --
    @staticmethod
    def rules():
        print('Game Rules:\n')
        print('You will choose how many questions you want to answer, each question has a score of 1.')
        print('You may quit the application after you have answer a question...')
        print('have in mind that by doing so, you will be score for the amount of questions you chose at the beginning')
        print('At the end the game will give you a score based of 100')
        print('This is an OSI challenge so your answer should be as follows: \n')
        print('Layer 1, or Layer 2. Basically the word layer followed by the layer number you think is the answer.')
        print('Good luck!!!')
        time.sleep(7.5)
        os.system('cls')


questions = Pool()
menu = Menu()


def main():
    print(f'Welcome to the OSI model game')
    if len(questions.items) == 0:
        print('There are no questions in the pool. The game cannot start with an empty list. \n')
        print('Please add questions to the pool. \n')
        print('Closing App.')
        sys.exit(0)
    else:
        print(f'\nPlease choose one of the following options: ')
        option = menu.options()
        while option != 'q':
            if option == '1':
                print(questions)
                print(f'\nPlease choose one of the following options: ')
                option = menu.options()
            elif option == '2':
                questions.check_pool()
                print(f'\nPlease choose one of the following options: ')
                option = menu.options()
            elif option == '3':
                questions.shuffle()
                menu.rules()
                i = int(input('\nHow many questions do you want to answer? :'))
                while i <= 0 or i > len(questions.items):
                    print(f'\nPlease enter a positive number between 1 and {len(questions.items)}.')
                    i = int(input('\nHow many questions do you want to answer? :'))
                else:
                    return i
        else:
            print('Good bye...')
            sys.exit(0)


play = Game(questions, main())
play.get_question()
