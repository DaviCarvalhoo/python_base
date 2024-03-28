from scraping import get_jobs
from flask import Flask, render_template, request, redirect, send_from_directory
from save import save_csv

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
    save_csv(search_result)
  else:
    return redirect('/')
  return render_template('result.html', jobs=search_result, keyword=keyword)

@app.route('/download/<filename>')
def download_file(filename):
  try:
    return send_from_directory('/home/davi/git_projects/python_base/static', filename=f"{filename}.csv", as_attachment=True)
  except:
    return redirect('/')

app.run(host='0.0.0.0')



