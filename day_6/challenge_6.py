import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
os.system("clear")
33

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
headers = {'User-Agent': user_agent}

url_iban = "https://www.iban.com/currency-codes"
url_transfwewise = 'https://wise.com/gb/currency-converter/'
countries = []


def ask_country(msg):
  print(msg)
  try:
    choice = int(input("#: "))
    if choice > len(countries):
      print("Escolha um pais da lista:")
      return ask_country(msg)
    else:
      print(f"Voce escolheu: {countries[choice]['name']}")
      return countries[choice]
  except ValueError:
    print("Isso nao e um numero!")
    return ask_country(msg)

def ask_amount(money_from, money_to):
  try:
    print(f"Quantos {money_from['code']} voce quer convertar para {money_to['code']}?")
    amount = float(input("#: "))
    return amount
  except ValueError:
    print("isso nao e um numero!")
    return ask_amount(money_from, money_to)

request = requests.get(url_iban)
soup = BeautifulSoup(request.text, "html.parser")
table = soup.find("table")
rows = table.find_all("tr")[1:]
for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code = items[2].text

  if code == '':
    continue
  else:
    country = {
      'name':name.capitalize(),
      'code': code
      }
    countries.append(country)

print("Bem vindo ao negociador de moedas!\nEscolha pelo numero da lista o pais que deseja consultar o codigo da moeda.\n")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")


money_from = ask_country('\n qual o pais de origem do dinheiro?')
money_to = ask_country('\n qual o pais de destino do dinheiro?')
amount = ask_amount(money_from, money_to)


from_code = money_from['code']
to_code = money_to['code']


tw_request = requests.get(f"{url_transfwewise}{from_code}-to-{to_code}-rate?amount={amount}", headers={'User-Agent': user_agent})
tw_soup = BeautifulSoup(tw_request.text, "html.parser")

rate = float(tw_soup.find('span', class_='text-success').string)


rate_math = amount * rate
print(format_currency(rate_math, to_code))