from flask import Flask

app = Flask("maratonaScraping")

@app.route('/')
def hello_world():
  return "Olá, mundo!"

@app.route('/<user>')
def welcome(user):
 return f"Bem vindo {user}"

app.run(host='0.0.0.0')
