import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    
}
# ascii = https://patorjk.com/software/taag/
print("""
██╗  ██╗████████╗██████╗ ██████╗     ████████╗███████╗███████╗████████╗
██║  ██║╚══██╔══╝██╔══██╗██╔══██╗    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
███████║   ██║   ██████╔╝██████╔╝       ██║   █████╗  ███████╗   ██║   
██╔══██║   ██║   ██╔═══╝ ██╔═══╝        ██║   ██╔══╝  ╚════██║   ██║   
██║  ██║   ██║   ██║     ██║            ██║   ███████╗███████║   ██║   
╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝            ╚═╝   ╚══════╝╚══════╝   ╚═╝       
""")
def menu():
    escolha = str(input("Verificar mais site s/N: ")).lower().strip()
    if escolha == "s":
        main()
    else:
        print("Programa encerrado.")
        return
    
def main():
    urls = str(input("Digite urls(separadas por virgula): ")).lower().split(",")
    for url in urls:
        url = url.strip()
        if "." not in url:
            print(url, "=== url inválida")
        elif "http://" not in url and "https://" not in url:
            url = f"https://{url}"
            try:
                rq = requests.get(url, headers=headers)
                print(url +"  ===  "+str(rq.status_code))
            except:
                print(f"{url} === url inválida")
        else:
            try:
                rq = requests.get(url, headers=headers)
                print(url +"  ===  "+str(rq.status_code))
            except:
                print(f"{url} === url inválida")
    menu()
main()