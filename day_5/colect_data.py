import cloudscraper
from bs4 import BeautifulSoup
scraper = cloudscraper.create_scraper()

print("""                                                                        
 $$$$$$$\ $$\   $$\  $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$$\ $$\   $$\ 
$$  _____|$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|$$ |  $$ |
$$ /      $$ |  $$ |$$ |  \__|$$ |  \__|$$$$$$$$ |$$ |  $$ |$$ /      $$ |  $$ |
$$ |      $$ |  $$ |$$ |      $$ |      $$   ____|$$ |  $$ |$$ |      $$ |  $$ |
\$$$$$$$\ \$$$$$$  |$$ |      $$ |      \$$$$$$$\ $$ |  $$ |\$$$$$$$\ \$$$$$$$ |
 \_______| \______/ \__|      \__|       \_______|\__|  \__| \_______| \____$$ |
                                                                      $$\   $$ |
                                                                      \$$$$$$  |
                                                                       \______/ """)

url_work = "https://www.iban.com/currency-codes"
r = scraper.get(url_work)
html = r.text
soup = BeautifulSoup(html, 'html.parser')


tabela = soup.find("table")
linhas = tabela.find_all("tr")[1:]

todos_paises = []

for linha in linhas:
    items = linha.find_all("td")
    nome = items[0].text
    moeda_codigo = items[2].text
    moeda_nome = items[1].text

    if moeda_nome != "No universal currency":
        pais = {
        'nome': nome,
        'codigo': moeda_codigo
        }
        todos_paises.append(pais)

def menu():
    try:
        escolha = int(input("Qual numero? >> "))
        if escolha > len(todos_paises):
            print('numero fora da lista, ecolha outro.')
            menu()
        else:
            resultado = todos_paises[escolha]
            print(f"Você escolheu: {resultado['nome']}, a moeda dele é {resultado['codigo']}")
    except:
        print("numero inválido(tente novamente)")
        menu()

for id, pais in enumerate(todos_paises):
    print(f"{id} - {pais['nome']}")
menu()