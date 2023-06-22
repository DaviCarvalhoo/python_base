list = [{"nome": "Davi"},{"nome": "Daniel"},{"nome": "Davi"},{"nome": "Daniel"},{"nome": "Davi"},{"nome": "Daniel"},{"nome": "Davi"},{"nome": "Daniel"}]
num=0
parada = 5
for nome in list:
    print(f"{nome['nome']} tem a posição: " + str(num))
    num+=1
    if num > parada: 
        break