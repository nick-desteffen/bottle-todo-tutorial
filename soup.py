from bs4 import BeautifulSoup
import urllib
import re

## Get the content
date = '121009'
url = "http://apod.nasa.gov/apod/ap%s.html" % (date)
page = urllib.urlopen(url)
html = page.read()

## Repair crappy markup
start_indexes = []
index = 0
for m in re.finditer('<p>', html):
  index = index + 1
  if index % 2 == 0:
    start_indexes.append(m.start())
  
for index in start_indexes:
  html = html[:(index + 2)] + "/" + html[(index + 2):]

## Parse HTML and break out pieces
soup = BeautifulSoup(html)
centers = soup.find_all('center')
paragraphs = soup.find_all('p')

## Find the image paths
high_res_image_path = centers[0].find_all("a")[1].get("href")
image_path = centers[0].img.get("src")

## Find the title
title = centers[1].find_all("b")[0].text.strip()

## Find the info
info = paragraphs[2]

print title
print high_res_image_path
print image_path
print info
