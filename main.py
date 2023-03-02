import requests
from bs4 import BeautifulSoup

country=input("what country you want to search ")
url=("https://en.wikipedia.org/wiki/"+country)

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

history_span = soup.find(id="History")
history_title = history_span.parent
history_p_tag = history_title.find_next_sibling("p")
history_h_tag = history_title.find_next_sibling("h2")
history_tag_3=history_h_tag.find_previous_sibling("p")
next_p=history_p_tag.find_next_sibling("p")

print(history_p_tag.text)
while next_p != history_tag_3:
 print(next_p.text)
 next_p = next_p.find_next_sibling("p") 
print(history_tag_3.text)
