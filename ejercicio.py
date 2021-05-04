palabra = ['c','a','m','a','s']
oculta = ["_"] * len(palabra)
word_string = " "

# while "_" in oculta:
#     letter = input("Ingresa Letra: ")
#     for i in range(len(palabra)): 
#         if letter in palabra[i]:
#             oculta[i] = letter
#             print("yes")
#         else:
#             print("NO")
#     print(oculta)


for i in range(len(palabra)):
    word_string = word_string + palabra[i]
print(word_string)
