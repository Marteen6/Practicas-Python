def palindrome():
    string = input("texto?: ")
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar cadena vacia")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False




if __name__ == '__main__':
    try:
        print(palindrome())
    except TypeError:
        print("Solo se pueden ingresar strings")

