def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Dame un numero: "))
        try:
            if num < 0:
                raise ValueError("Ingresar solo numeros positivos")
            print(divisors(num))
            print('Termino el programa')
        except ValueError as ve:
            print(ve)
    except ValueError:
        print('Solo ingresar numeros')

    
if __name__ == '__main__':
    run()