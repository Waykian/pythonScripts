import fetchRandomWikipediaPage

while True:
    title = fetchRandomWikipediaPage.getTitle()
    print("Do you want to read the article \"" + title + "\"? (y/n)")
    check = input()
    match check:
        case ('y'|'Y'):
            fetchRandomWikipediaPage.fetch(title)
        case ('n'|'N'):
             continue
        case _:
            print("Quitting the program")
            quit()

