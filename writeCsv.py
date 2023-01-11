import csv

def writecsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file: # W = re-write file // A = Update file 
        fw = csv.writer(file)
        fw.writerow(data)

writecsv()