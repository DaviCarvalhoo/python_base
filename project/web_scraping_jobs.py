import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", 
}
url_work = "https://www.empregos.com.br/vagas/programador-python/"
r = requests.get(url_work, headers=headers)
html = r.text
soup = BeautifulSoup(html, 'html.parser')
cards = soup.find('div', id="ctl00_ContentBody_divPaiMioloBusca")
items = cards.find_all("li", class_="item")

jobs = []

for item in items:
  try:
    job = {
      'title':item.find('h2').find('a').get_text().strip(),
      'company': item.find('span', class_="nome-empresa").find('a').get_text().strip(),
      'location': item.find('span', class_="nome-empresa").get_text().strip().replace("\n", "").replace("-", "", 1).split('\r', 1)[-1].strip(),
      'how_old': item.find('span', class_="publicado").get_text(),
      'link': item.find('h2').find('a').get('href')
    }
    jobs.append(job)   
  except:
    continue

print(jobs)