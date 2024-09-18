import requests
from bs4 import BeautifulSoup

url = 'https://thehockeynews.com/news'

proxies = {
    'http': 'http://127.0.0.1:9090',
    'https': 'https://127.0.0.1:9090',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

print(response.reason)
print(response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
else:
    print("Request blocked or failed")
