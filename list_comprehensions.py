def run():
    # squares = []
    # # for i in range(1, 101):
    # #     if i % 3 != 0:
    # #         squares.append(i**2)

    listcomprehension = [i for i in range(1,10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
        
    print(listcomprehension)

   

if __name__ == '__main__':
    print('welcome')
    run()