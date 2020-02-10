# ==================================================================================================================
# @title          :app.py
# @description    :This is the game for the Networking Class
# @author         :Sergio Guzman @ sergio.guzman@blackboard.com
# @date           :2020-01-24
# @version        :1.0
# @usage          :app.py
# ==================================================================================================================

import os
import sys
import time
from random import shuffle

# -- Pool of questions and answers respectively --
pool = [
    ['Messenger como una herramienta para transmisión de texto on-line con otra persona, lo podemos clasificar '
     'como parte de la capa en el sistema OSI como?', 'capa 7'],
    ['Outlook es una herramienta que nos ayuda a visualizar nuestros correos electrónicos se asocia con la capa?',
     'capa 7'],
    ['Se ha vuelto muy común que todos podamos reproducir videos de música, tutoriales, etc… este proceso que nos '
     'permite hacerlo se clasificaría en la capa?', 'capa 7'],
    ['El modelo que la ISO utilizo para estandarizar la compresión de la transmisión de información a través de la '
     'red se denomino OSI; este establece una capa que es el punto de inicio y fin del sistema, denominada?',
     'capa 7'],
    ['La capa que le permita al emisor y al receptor visualizar los datos transmitidos es?', 'capa 7'],
    ['La forma con la que interactuamos con las maquinas se ha logrado gracias a la capa?', 'capa 7'],
    ['Entrada y salida de datos es gracias a la capa?', 'capa 7'],
    ['La decodificación para la recepción-visualización y envio-transmision de información es explicado en la capa?',
     'capa 7'],
    ['Primera capa del emisor y ultima capa del receptor según el sistema OSI?', 'capa 7'],
    ['Si creas un documento, se clasifica este proceso en la capa? Según el modelo OSI.', 'capa 7'],
    ['Que capa se encarga de que recibas un documento texto y no otro tipo de archivo cuando te han enviado un '
     'documento en este formato?', 'capa 6'],
    ['La compilación de todos los paquetes asociados se completa en la capa?', 'capa 6'],
    ['Esta capa se encarga de realizar el envió de la información en paquetes?', 'capa 6'],
    ['Todos los paquetes deben estar completos para que la capa de _________ pueda pasar la información a la capa '
     'de Aplicación.',
     'capa 6'],
    ['Segunda y penúltima capa según el sistema de referencia OSI es:', 'capa 6'],
    ['Sabemos que toda la información es al final solo 0 y 1, pero gracias a la esta capa esos 0 y 1 se hacen '
     'visibles en documentos, videos, música al pasar a la capa de Aplicación.', 'capa 6'],
    ['Cada terminal tiene un dispositivo encargado de decodificar los paquetes de datos, esto es hecho en la capa?',
     'capa 6'],
    ['La codificación de los datos en paquetes para su transmision lo realizamos en esta capa:', 'capa 6'],
    ['Cuando tenemos perdida de velocidad en la red y los videos se empiezan a ver pixelados es porque la '
     'capa________ esta decodificando los paquetes que recibe, aunque estos no lleguen con la velocidad necesaria '
     'para mantener una buena calidad:', 'capa 6'],
    ['Toda la información que generamos es transmitida en paquetes gracias a todo los procesos de codificación y '
     'decodificación de datos que ocurre en la capa?', 'capa 6'],
    ['Esta capa se encarga de establecer de donde es enviado los paquetes?', 'capa 5'],
    ['Saber para donde va el paquete es crucial para direccionarlo correctamente, es por ello que la capa _______ '
     'agrega su destino:', 'capa 5'],
    ['Cada maquina y/o dispositivo debe estar plenamente identificado en la red para que pueda recibir y enviar '
     'información sin ningún problema. Esta identificación se realiza en la capa?', 'capa 5'],
    ['Se establece destinatario y destino?', 'capa 5'],
    ['Rotulo del paquete que permite identificar que ha llegado a su destinatario correcto, es establecido en la capa?',
     'capa 5'],
    ['Le permite a la red establecer de donde proviene el paquete para clasificarlo y tener una ruta devuelta en '
     'caso de recibir una respuesta.', 'capa 5'],
    ['Si un paquete no llega a su destino o la respuesta no es recibida de vuelta es porque el proceso de rotulado '
     'de origen/destino tuvo un error en la capa?', 'capa 5'],
    ['Aquí se permite la entrada de los paquetes siempre y cuando tengan el rotulo de envío o destino en el paquete.',
     'capa 5'],
    ['Si la capa de _______ no rotula los paquetes, el sistema no tiene como clasificar los paquetes.', 'capa 5'],
    ['Aquí permite ser identificado el emisor de los paquetes.', 'capa 5'],
    ['El protocolo TCP pertenece a la capa?', 'capa 4'],
    ['El protocolo UDP garantiza la transmisión correcta de los datos, pertenece a la capa?', 'capa 4'],
    ['El rechazo de paquetes dañados se realiza en la capa?', 'capa 4'],
    ['Los diferentes tipos de datos son enviados entre emisor y receptor, y todo este proceso es denominado la capa?',
     'capa 4'],
    ['En esta capa toma los paquetes e identifica su destino para despacharlos', 'capa 4'],
    ['Esta capa determina si los datos se van a enviar de manera segura o no Segura.', 'capa 4'],
    ['Toda la conexión de extremo a extremo.', 'capa 4'],
    ['Identifica el protocolo con el que se deben enviar el tipo de dato para que sean enviado óptimamente a '
     'través del sistema.', 'capa 4'],
    ['Se encarga de enviar todos los paquetes en conjunto para que que lleguen a su destino.', 'capa 4'],
    ['Hace llegar los paquetes según su rotulo de destino a su correcto destinatario.:', 'capa 4'],
    ['¿Qué capa es la que encarga de realizar el direccionamiento lógico y la determinación de la ruta de los datos?',
     'capa 3'],
    ['¿El protocolo IP (IPsec, IPv4, IPv6) es de la capa?', 'capa 3'],
    ['¿envía a los paquetes de nodo a nodo usando ya sea un circuito virtual o datagramas, en qué modelo OSI está?',
     'capa 3'],
    ['¿mapeo de direcciones lógicas a direcciones fisicas?', 'capa 3'],
    ['¿se encarga de controlar el funcionamiento de la sub red?', 'capa 3'],
    ['¿transfiere datos desde el host que origina hacia el host de llegada?', 'capa 3'],
    ['¿proceso de direccionamiento, encapsulamiento, enrutamiento, desencapsulamiento, son básicos en la  capa __?',
     'capa 3'],
    ['¿los routers trabajan en la capa__?', 'capa 3'],
    ['¿los firewalls actúan sobre la capa ?', 'capa 3'],
    ['¿utiliza un control de congestión y control de errores?', 'capa 3'],
    ['¿ son control lógicos (LLC)y control de acceso al medio (MAC)?', 'capa 2'],
    ['¿se encarga del direccionamiento físico?', 'capa 2'],
    ['¿se activa la detección de errores, distribución ordenada de tramas y control de flujo?', 'capa 2'],
    ['¿el dispositivo switch es el que maneja la capa?', 'capa 2'],
    ['¿dispositivo puente(BRIDGE) opera en la capa?', 'capa 2'],
    ['¿LAN, WAN es protocolo de capa?', 'capa 2'],
    ['¿una de las funciones son segmentación, bloqueo, control de flujo, de la capa_?', 'capa 2'],
    ['¿una trama incluye: datos, encabezado, tráiler. equivale a la capa?', 'capa 2'],
    ['¿ATM es protocolo de la capa?', 'capa 2'],
    ['¿PPP permite establecer comunicación a nivel de la capa de __?', 'capa 2'],
    ['¿medios físicos por donde viaja la comunicación, cables de red..etc,?', 'capa 1'],
    ['¿garantiza la conexión?', 'capa 1'],
    ['¿transmite el flujo de bits a través de los medios?', 'capa 1'],
    ['¿codificación de la señal?', 'capa 1'],
    ['¿es la que se encarga de la conexión física entre el nodo y la red?', 'capa 1'],
    ['¿manejan voltajes y pulsos eléctricos?', 'capa 1'],
    ['¿Cuándo se habla de par trenzado se habla de la capa?', 'capa 1'],
    ['¿la fibra óptica se relaciona con la capa?', 'capa 1'],
    ['¿manejan las señales eléctricas y electromagnéticas de los medios de transmisión?', 'capa 1'],
    ['¿topologías físicas de red,(bus, anillo, malla)?', 'capa 1']
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
            print(f'\nI\'m sorry, that\'s not correct. The correct answer was {correct_answer}.'
                  f' Your score is  {self.score}.\n')

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
            time.sleep(8.0)
            sys.exit(0)

    # -- Game Rules --
    @staticmethod
    def rules():
        print('Game Rules:\n')
        print('You will choose how many questions you want to answer, each question has a score of 1.')
        print('You may quit the application after you have answer a question...')
        print('have in mind that by doing so, you will be scored for the amount of questions you chose at the beginning')
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
                i = int(input('\nHow many questions do you want to answer?: '))
                while i <= 0 or i > len(questions.items):
                    print(f'\nPlease enter a positive number between 1 and {len(questions.items)}.')
                    i = int(input('\nHow many questions do you want to answer?: '))
                else:
                    return i
        else:
            print('Good bye...')
            time.sleep(7.5)
            sys.exit(0)


play = Game(questions, main())
play.get_question()
