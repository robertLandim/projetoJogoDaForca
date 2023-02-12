# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
from unidecode import unidecode
import random
from spellchecker import SpellChecker

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
        # Construir variavel da palavra oculta "____"
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
        print(f"Palavra: {''.join(self.hiddenWord)}")
        print(f"Letras erradas: {' '.join(self.incorrectLetters)}")
        print(f"Letras corretas: {' '.join(self.correctLetters)}")


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank)-1)].strip()


def adicionar_palavra():
    palavra = str(input("Digite a palavra que deseja adicionar:"))
    if validar_palavra(palavra):
        palavra = palavra.upper()
        palavra = unidecode(palavra)
        with open("palavras.txt", "r") as palavras:
            verifica_existencia = palavras.readlines()
        if palavra in verifica_existencia or palavra + "\n" in verifica_existencia:
            print(f"Esta palavra já existe no banco de dados do jogo, tente adicionar outra palavra!")
            adicionar_palavra()
        else:
            with open("palavras.txt", "a") as palavras:
                palavras.write("\n" + palavra)
            print(f"Palavra '{palavra}' adicionada com sucesso!")
    else:
        print(f"Palavra inválida, não é possível adicionar palavras com acentos ou números.\nTente novamente!")
        adicionar_palavra()


def validar_palavra(palavra):
    spell = SpellChecker(language='pt')
    if palavra in spell:
        return True
    else:
        return False


# Função Main - Execução do Programa
def main():
    # Objeto
    opcao = input("Digite uma opção:\n1 - Jogar\n2 - Adicionar palavras ao jogo\n3 - Sair do jogo\n")
    if opcao not in ["1", "2", "3"]:
        print("Opção inválida!")
        main()
    elif opcao == "1":
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
            print(f'\nParabéns! Você venceu!!')
            print(f'A palavra era: {game.word}')
        else:
            print('\nGame over! Você perdeu.')
            print(f'A palavra era: {game.word}')
        print('\nFoi bom jogar com você! Agora vá estudar!\n')
        main()
    elif opcao == "2":
        adicionar_palavra()
        main()


# Executa o programa
if __name__ == "__main__":
    main()

