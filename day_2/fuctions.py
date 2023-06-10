nome = "davi carvalho"
def welcome(nome):
    msg = "Oi " +nome.title() + ", tudo bom?"
    print(msg)

def name(name="Davi"):
    print(f"Olá, {name}")

def plus(n1=0,n2=0):
    print(n1+n2)

welcome(nome)
name()
plus(10,30)