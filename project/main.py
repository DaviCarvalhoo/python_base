from scraping import get_jobs
from flask import Flask, render_template, request, redirect

app = Flask("maratonaScraping")

@app.route('/')
def hello_world():
  return render_template('search.html')

@app.route('/search.html')
def welcome():
 return render_template('search.html')

@app.route('/result')
def result():
  keyword = request.args.get('keyword')
  keyword = keyword.lower()
  if keyword:
    search_result = get_jobs(keyword)
  else:
    return redirect('/')
  return render_template('result.html', jobs=search_result)

app.run(host='0.0.0.0')



