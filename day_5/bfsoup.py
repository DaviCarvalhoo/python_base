import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", 
}
url_work = "https://www.workana.com/pt/jobs?language=pt&skills=qa-automation"
r = requests.get(url_work, headers=headers)
html = r.text
soup = BeautifulSoup(html, 'html.parser')
print(soup.find_all(class_="project-item js-project"))