import requests

URL  = input("Enter a url to bruteforce: ").strip()
FILE = input("Enter the full path to you list: ").strip()

with open(FILE,'r') as text:
	LIST = text.readlines()
	LIST = ''.join(LIST)
	NEW = LIST.split()

for path in NEW:

	RESPONSE = requests.get(URL+'/'+path)

	print(f"{URL}/{path} {RESPONSE.status_code}")
