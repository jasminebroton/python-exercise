from movies import Movies

movies = Movies('./movies.txt')

while True:
    user_input = input("\nMenu \nq: quit\nlist: print out all movie names\nsn: search movie names\nsc: search casts\n")
    if user_input == 'q':
        break
    elif user_input == 'list':
        movies.prints()
    elif user_input == 'sn':
        name_input = input("What movie would you like to search?\n")
        movies.search(name_input)
    elif user_input == 'sc':
        cast_input = input("What actor would you like to search for?\n")
        movies.searchCast(cast_input)
    else:
        print('Invalid input, try again!')
