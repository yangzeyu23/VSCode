import urllib.request

url = 'http://localhost:8080/NoteWebService/note.do?action=query&ID=10'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
	data = response.read()
	json_data = data.decode()
	print(json_data)






















