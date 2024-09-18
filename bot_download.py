import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.namasha.com/search?q=فیلم سینمایی هتل'

response = requests.get(url)
print(response.reason)
content = BeautifulSoup(response.text, 'html.parser')
#print(content)
links = content.find_all('a', href=re.compile('^https'))
for link in links:
    pass

print(links)

# class ScraperVideo:
#     def __init__(self, subject: str):
#         self.subject = str(subject)
#     def generate_url(self):
#         return f'https://www.namasha.com/search?q={self.subject}'
#
#
#


# a = ScraperVideo(subject='فیلم سینمایی هتل')
#
# url = a.generate_url()
# response = requests.get(url)
# print(response.reason)