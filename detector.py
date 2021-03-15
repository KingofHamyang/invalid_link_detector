import requests
from bs4 import BeautifulSoup


indexed_pages = {}
already_lookup = {}

def page_lookup(url):
  soup = BeautifulSoup(requests.get(url).text, 'html.parser')
  links = soup.find_all("a")
  page_to_lookup = []
  print("links in page : " + str(url))
  print("=======================================================")
  for link in links:

    href = link.attrs.get('href')
    if not href:
      continue
    text = link.string
    if not text:
      text = 'None'
    if 'oslab.kaist.ac.kr' in href and '.' not in href[str(href).rindex('/'):]:
      page_to_lookup.append(href)
    else :
      if 'http' not in href:
        continue
      else:
        if href not in indexed_pages:
          indexed_pages[href] = 1
          print(text + ' > ', end='')
          print(href)
  for page in page_to_lookup:
    if page not in already_lookup:
      already_lookup[page] = 1
      page_lookup(page)





url = 'https://oslab.kaist.ac.kr/'
page_lookup(url)