import requests
file_id = '1Z9Oc70TOGOK4_QuCnvUYyxiQFQccc3L3c79jrwuLDGo'
url = 'https://docs.google.com/spreadsheets/d/{0}/export?format=csv".format(file_id)'
#print("Hello World")

r = requests.get(url)
