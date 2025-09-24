import requests
from bs4 import BeautifulSoup


url = requests.get('https://quotes.toscrape.com/tag/inspirational/') 

soup = BeautifulSoup(url.text, 'html.parser')

#two lists for quotes and author
quotes = []
all_authors = []

#check if the server response is OK
def check_server():
    if url.status_code == 200:
        txt = soup.select('span.text')
        author = soup.select('small.author')
        for span in txt:
            quotes.append(span.get_text())
        for a in author:
            all_authors.append(a.get_text())
    else:
        print('Something wrong!')

#call the function
check_server()

#create a dict, quote by author
result = {}

#check len, must be same len for author and quotes
if len(quotes) == len(all_authors):
    for i in range(len(all_authors)):
        key = all_authors[i]
        v = quotes[i]
        if key not in result:
            result[key] = []
        result[key].append(v)

#work with file
def write_in_file():
    with open('quotes.csv', 'w', encoding='utf-8') as file:
        for k, v_list in result.items():
            for v in v_list:
                line = f'"{v}" - {k}\n'
                file.write(line)

