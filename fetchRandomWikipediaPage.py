import re
import requests
from bs4 import BeautifulSoup
 
url = "https://en.wikipedia.org/w/api.php"

def getTitle():
    # Fetch the title of the random page
    params = {
        "action": "query",
        "list": "random",
        "format": "json",
        "rnnamespace":"0",
        "rnlimit":"1"
    }

    response = requests.get(url, params = params)
    data = response.json()
    return data["query"]["random"][0]["title"]

subject = getTitle()

#Fetch the actual page
params = {
    "action": "parse",
    "page": subject,
    "format": "json",
    "prop":"text",
    "redirects":""
}
 
response = requests.get(url, params=params)
data = response.json()

raw_html = data["parse"]["text"]["*"]
soup = BeautifulSoup(raw_html,"html.parser")
text = ""

#Put all paragraphs of the page together
for p in soup.find_all("p"):
    text += p.text

#Remove citation numbers
text = re.sub("\[[0-9]+\]", "", text)

#Print title and text
print(subject)
print(text)
