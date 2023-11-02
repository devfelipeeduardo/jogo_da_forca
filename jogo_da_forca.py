import random


print("-"*34)
print("    Bem vindo ao jogo da Forca    ")
print("-"*34)

#Listas
words = ['salamandra', 'papel', 'cassino', 'arrozinho', 'placas', 'potes', 'jarras', 'taça'] #Palavras

#Escolhe a palavra

def choose_word():
    return random.choice(words) 

def play_hangman(word):
    
    #Counters
    corrects_letters = []
    attempts = 6

    #Make a hidden word
    hidden_word = ['_'] * len(word) 

    #LOOP
    while attempts > 0:

        #Mostra Palavra, tentativa, e pede uma letra para o jogador.
        print("Palavra: " + " ".join(hidden_word))
        print(f"Você possue {attempts} tentativas!")
        letter = input('Escolha uma letra: ').lower()


        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
                    corrects_letters.append(letter)
        else:
            print("Letra incorreta. Tente novamente!")
            attempts -= 1


        if "".join(hidden_word) == word:
            print(f"Parabéns, você venceu! A palavra era: {word.capitalize()}")
            break


    if attempts == 0:
        print("Suas tentativas acabaram! Tente novamente! ")


play_hangman(choose_word())
