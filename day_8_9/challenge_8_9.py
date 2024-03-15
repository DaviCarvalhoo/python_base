import requests
from flask import Flask, render_template, request

app = Flask('MaratonanEWS')

@app.route('/')
def home():
  order_by = request.args.get("order_by")
  if order_by == 'news':
    url = 'https://hn.algolia.com/api/v1/search_by_date?tags=story'
  else:
    url = 'https://hn.algolia.com/api/v1/search?tags=story'
    
  result = requests.get(url).json()["hits"]
  return render_template('news.html', results=result, order_by=order_by)

@app.route('/<id>')
def by_id(id):
  url = f"http://hn.algolia.com/api/v1/items/{id}"
  results = requests.get(url).json()
  return render_template('id.html', results=results)

app.run(host='0.0.0.0')