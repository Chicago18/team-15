import csv
import io
import requests
file_id = '1Z9Oc70TOGOK4_QuCnvUYyxiQFQccc3L3c79jrwuLDGo'
url = 'https://docs.google.com/spreadsheets/d/{0}/export?format=csv".format(file_id)'
#print("Hello World")

r = requests.get(url)

#print(r.text)
sio = io.StringIO(r.text, newline=None)
reader = csv.reader(sio, dialect=csv.excel)
rownum = 0
data = {}
cols=[]
for row in reader:
	if rownum == 0:
		for col in row:
			data[col] = ''
			cols.append(col)
	else:
		i = 0
		for col in row:
			data[cols[i]] = col
			i=i+1
		print(data)
	rownum = rownum+1


