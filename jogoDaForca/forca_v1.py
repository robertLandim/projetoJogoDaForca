# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

    +---+
    |   |
    |
    |
    |
    |
===========''', '''

    +---+
    |   |
    |   O
    |
    |
    |
===========''', '''

    +---+
    |   |
    |   O
    |   |
    |
    |
===========''', '''

     +---+
     |   |
     |   O
     |  /|
     |
     |
===========''', '''

     +---+
     |   |
     |   O
     |  /|\\
     |
     |
===========''', '''

     +---+
     |   |
     |   O
     |  /|\\
     |  /
     |
===========''', '''

     +---+
     |   |
     |   O
     |  /|\\
     |  / \\
     |
===========''']


class Hangman:

    # Método Construtor
    def __init__(self, word=''):
        self.word = word.upper()
        self.incorrectLetters = []
        self.correctLetters = []
        self.statusBoard = 0
        # construir variavel da palavra oculta "____"
        self.hiddenWord = []
        for l in self.word:
            self.hiddenWord.append('_')

    # Método para adivinhar a letra
    def guess(self, letter):
        self.letter = letter
        if self.letter in self.word:
           self.correctLetters.append(self.letter)
        else:
            self.statusBoard += 1
            self.incorrectLetters.append(self.letter)

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.statusBoard == len(board) - 1:
            return True
        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if len(list(filter(lambda x: x=='_', self.hiddenWord))) == 0:
            print(str(self.hiddenWord).find("_"))
            return True
        else:
            return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        for i, l in enumerate(self.word):
            if l == self.letter:
                self.hiddenWord[i] = self.letter

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[self.statusBoard])
        print(f"Palavra: {self.hiddenWord}")
        print(f"Letras erradas: {self.incorrectLetters}")
        print(f"Letras corretas: {self.correctLetters}")


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank)-1)].strip()

# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())
    letter = ''
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_won() and not game.hangman_over():
        # Verifica o status do jogo
        game.print_game_status()
        while letter in game.correctLetters or letter in game.incorrectLetters:
            letter = str(input("Digite uma letra: ")).upper()
            if letter != '' and letter in game.correctLetters or letter in game.incorrectLetters:
                print("!!! Esta letra já foi digitada !!!")
        game.guess(letter)
        game.hide_word()

    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()

