from movies import Movies

movies = Movies('./movies.txt')

while True:
    user_input = input("Menu \nq: quit\nlist: print out all movie names")
    if user_input == 'q':
        break
    elif user_input == 'list':
        movies.prints()
    else:
        print('Invalid input, try again!')
