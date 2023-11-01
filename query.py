from movies import Movies

movies = Movies('./movies.txt')

while True:
    user_input = input("Menu: \nq: quit")
    if user_input == 'q':
        break
    else:
        print('Invalid input, try again!')
