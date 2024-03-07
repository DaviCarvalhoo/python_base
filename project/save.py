import csv

def save_csv(jobs):
  file = open('project/jobs.csv', 'w')
  write = csv.writer(file)
  write.writerow(['title','company','location', 'how_old', 'link'])
