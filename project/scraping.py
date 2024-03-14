from web_scraping_jobs import scraping, key
from save import save_csv

def get_jobs(keyword):
  result = key(keyword)

  return result