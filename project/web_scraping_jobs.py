import requests
from bs4 import BeautifulSoup

url = "https://www.empregos.com.br/vagas/programador-"


def key(keyword):
  r_key = requests.get(f"{url}{keyword}")
  html = r_key.text
  soup = BeautifulSoup(html, 'html.parser')

  pages_l = soup.find("div", class_="pagination-list").find('ul').find_all('li')
  n_pages = []
  for n in pages_l:
    number = n.get_text().strip()
    n_pages.append(number)

  urls = []
  for page in n_pages:
    new_url = f"{url}{keyword}/p{int(page)}"
    urls.append(new_url)

  return scraping(urls)


def scraping(urls):
  all_jobs = []
  for url in urls:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", 
    }
    
    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find('div', id="ctl00_ContentBody_divPaiMioloBusca")
    items = cards.find_all("li", class_="item")

    for item in items:
      try:
        job = {
          'title':item.find('h2').find('a').get_text().strip(),
          'company': item.find('span', class_="nome-empresa").find('a').get_text().strip(),
          'location': item.find('span', class_="nome-empresa").get_text().strip().replace("\n", "").replace("-", "", 1).split('\r', 1)[-1].strip(),
          'how_old': item.find('span', class_="publicado").get_text(),
          'link': item.find('h2').find('a').get('href')
          }
        all_jobs.append(job)   
      except:
        continue
  return all_jobs
