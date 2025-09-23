import requests
from bs4 import BeautifulSoup


url = requests.get('https://quotes.toscrape.com/tag/inspirational/') 

soup = BeautifulSoup(url.text, 'html.parser')

#two lists for quotes and author
quotes = []
all_authors = []

#check if the server response is OK
if url.status_code == 200:
    txt = soup.select('span.text')
    author = soup.select('small.author')
else:
    error = 'Something wrong!'

#add all quotes 
for span in txt:
    quotes.append(span.get_text())

#add all authors 
for a in author:
    all_authors.append(a.get_text())

#create a dict, quote by author
result = {}

#check len, must be same len for author and quotes
if len(quotes) == len(all_authors):
    for i in range(len(all_authors)):
        key = all_authors[i]
        v = quotes[i]
        result[key] = v


#work with file
with open('quotes.csv', 'w', encoding='utf-8') as file:
    for k, v in result.items():
        line = ""+ v + "" + '-' + "" + k + ""+ '\n'
        file.write(line)

