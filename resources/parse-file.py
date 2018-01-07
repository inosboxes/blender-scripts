import pandas as pd
from bs4 import BeautifulSoup
from sets import Set
import itertools
from pprint import pprint

def parseHtmlTableFile(path):
  """docstring for parseHtmlTableFile"""

  with open(path, 'r') as content_file:
    html_string = content_file.read()

  soup = BeautifulSoup(html_string)

  headers = []
  planets = []
  rows = []

  for header in soup.select("th"):
    headers.append(header.get_text(strip=True))

  headers = headers[0:len(headers)/2]

  for row in soup.select("tr"):
    cells = []
    for cell in row.find_all('td'):
      cells.append( cell.get_text(strip=True))

    if len(cells) <> 0:
      rows.append(cells)

  for planet in rows:
      adict = dict(itertools.izip(headers,planet))
      planets.append(adict)

  return planets

def parseFiles(files):
  """docstring for parseFiles"""
  collection = []
  for path in files:
    data = parseHtmlTableFile(path)
    collection.append({'source': path, 'data': data})
  return collection

files = [
  'planets-orbital-properties.html',
  'planets-Atmospheres.html',
  'planets-physical-Characteristics.html'
]

pprint(parseFiles(files))
