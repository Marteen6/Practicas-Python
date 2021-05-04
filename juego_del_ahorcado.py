import random

ahorcado = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def random_word():
    #Se obtiene una pabra al azar de la lista 'data.txt'
    all_words = []
    word = []
    with open("./data.txt", "r", encoding="utf-8") as d:
        for item in d:
            all_words.append(item.replace("\n", ""))
        selected_word = all_words[random.randint(0,170)]
        for i in range(len(selected_word)):
            word.append(selected_word[i])
        return word

def word_string(word):
    #Convierte la palabra de lista a string
    word_string = " "
    for i in range(len(word)):
        word_string = word_string + word[i]
    return word_string.upper()

def choose_letter(word):
    ok = False
    while ok == False:
        letter = input("Ingresa una letra: ")
        if letter != "":
            ok = True
    print(letter)
    return letter



def compare(word):
    # # Compara las letras del jugador y las de la palabra
    life = 0
    hidden_word = ["_"] * len(word)
    final_word = word_string(word)
    print(f"----------------------\n{hidden_word}")

    while life < 6 and "_" in hidden_word:
        letter = choose_letter(word)
        correcto = False
        for i in range(len(word)):
            if letter in word[i]:
                hidden_word[i] = letter
                correcto = True
            else:
                continue
            
        if correcto != True:
            life+=1
            print(f"Fallaste")
            print(ahorcado[life])
        print(f"\n\n{hidden_word}")

        if life == 6:
            print(f"\n\nSe terminaron las oportunidades, la palabra era:{final_word.upper()}\n\n")
        elif "_" not in hidden_word:
            print(f"\n\nMuy Bien! La palabra era:{final_word.upper()}\n\n")
                

if __name__ == '__main__':
    print("\nAdivina la palabra")
    word = random_word()
    compare(word)
