import requests  

site = "https://www.workana.com/pt/jobs?language=pt&skills=qa-automation"
r = requests.get(site)
print(r.status_code)