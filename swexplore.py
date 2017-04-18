from swfunc import *

filmurl = "http://swapi.co/api/films"

films = getAllPages(filmurl)
print('\nFilms:')
printItems(films, "title")
done = False
while not done:
    choice = input('\n==> Enter the number of the film you would like to explore: ')
    try:
        if choice.lower() == 'q':
            done = True
            continue
        else:
            film = films[int(choice) - 1]
    except:
        print('Invalid entry: ' + choice + '. Try again!')
        continue

    while not done:
        print('Current film: ' + film["title"])
        choice = input("\n==> Would you like to explore the characters (C), planets (P), vehicles (V), starships (S), or attributes (A) of %s? Select one: " % (film["title"]))
        print('')

        if choice.lower() == 'c':
            urls = film["characters"]
            print('Characters: ')
            chars = getItemList(urls, "name")
            promptForItem(chars, "character")

        elif choice.lower() == 'p':
            urls = film["planets"]
            print('Planets: ')
            planets = getItemList(urls, "name")
            promptForItem(planets, "planet")

        elif choice.lower() == 'v':
            urls = film["vehicles"]
            print('Vehicles: ')
            vehicles = getItemList(urls, "name")
            promptForItem(vehicles, "vehicle")

        elif choice.lower() == 's':
            urls = film["starships"]
            print('Starships: ')
            starships = getItemList(urls, "name")
            promptForItem(starships, "starship")

        elif choice.lower() == 'a':
            printAttributes(film)
            print('')

        elif choice.lower() == 'q':
            done = True

        else:
            print('Invalid entry. Try again!')
            continue
