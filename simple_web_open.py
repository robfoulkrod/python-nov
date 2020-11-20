import urllib.request

url = "https://api.github.com/users/robfoulkrod"

response = urllib.request.urlopen(url)

print(response.info())


content = response.read(1260).decode()

print(content)
