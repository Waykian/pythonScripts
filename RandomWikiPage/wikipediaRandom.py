import subprocess
from bs4 import BeautifulSoup


import sys
print(sys.version)

while True:
    check = input("Do you want to read the article? ")
    match check:
        case ('y'|'Y'):
            p = subprocess.run(["python", "RandomWikiPage/fetchRandomWikipediaPage.py"])
        case ('n'|'N'):
            continue
        case _:
            print("Quitting the program")
            quit()

