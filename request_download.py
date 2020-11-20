import requests

url = 'https://github.com/robfoulkrod/python-nov/raw/main/materials/py3master_1.9.zip'
local_name = 'py.zip'

with requests.get(url, stream=True) as response:
    response.raise_for_status()
    with open(local_name, "wb") as output_file:
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                output_file.write(chunk)

print("Downloaded the file!")
