from movies import Movies

movies = Movies('./movies.txt')

while True:
    user_input = input("Menu \nq: quit\nlist: print out all movie names\nsn: search movie names\n")
    if user_input == 'q':
        break
    elif user_input == 'list':
        movies.prints()
    elif user_input == 'sn':
        name_input = input("What movie would you like to search?")
        movies.search(name_input)
    else:
        print('Invalid input, try again!')
