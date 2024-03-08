import csv

def save_csv(jobs):
  file = open('project/jobs.csv', 'w')
  write = csv.writer(file)
  write.writerow(['title','company','location', 'how_old', 'link'])
  for job in jobs:
    write.writerow(list(job.values()))
    # write.writerow([job['title'], job['company'],job['location'], job['how_old'], job['link']])
