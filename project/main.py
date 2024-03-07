from web_scraping_jobs import scraping, key
from save import save_csv

result = scraping(["https://www.empregos.com.br/vagas/programador-python"])

save_csv(result)